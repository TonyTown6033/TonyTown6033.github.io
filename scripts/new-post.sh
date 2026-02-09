#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  scripts/new-post.sh "<title>" [--slug your-slug] [--section posts] [--publish]

Examples:
  scripts/new-post.sh "My first post"
  scripts/new-post.sh "My first post" --slug my-first-post
  scripts/new-post.sh "Release notes" --publish
EOF
}

slugify() {
  local input="$1"
  local slug

  slug="$(
    printf '%s' "$input" \
      | tr '[:upper:]' '[:lower:]' \
      | sed -E 's/[[:space:]]+/-/g; s/[^a-z0-9-]//g; s/-+/-/g; s/^-+//; s/-+$//'
  )"

  if [ -z "$slug" ]; then
    slug="$(date +%Y%m%d-%H%M%S)"
  fi

  printf '%s' "$slug"
}

if [ "${1:-}" = "-h" ] || [ "${1:-}" = "--help" ]; then
  usage
  exit 0
fi

if [ "$#" -lt 1 ]; then
  usage
  exit 1
fi

if ! command -v hugo >/dev/null 2>&1; then
  echo "Error: hugo not found in PATH." >&2
  exit 1
fi

title="$1"
shift

slug=""
section="posts"
publish=0

while [ "$#" -gt 0 ]; do
  case "$1" in
    -h|--help)
      usage
      exit 0
      ;;
    --slug)
      shift
      if [ "$#" -lt 1 ]; then
        echo "Error: --slug requires a value." >&2
        exit 1
      fi
      slug="$1"
      ;;
    --section)
      shift
      if [ "$#" -lt 1 ]; then
        echo "Error: --section requires a value." >&2
        exit 1
      fi
      section="$1"
      ;;
    --publish)
      publish=1
      ;;
    *)
      echo "Error: unknown option '$1'." >&2
      usage
      exit 1
      ;;
  esac
  shift
done

if [[ ! "$section" =~ ^[a-zA-Z0-9/_-]+$ ]]; then
  echo "Error: section contains invalid characters." >&2
  exit 1
fi

if [ -z "$slug" ]; then
  slug="$(slugify "$title")"
fi

if [[ ! "$slug" =~ ^[a-z0-9][a-z0-9-]*$ ]]; then
  echo "Error: slug must match ^[a-z0-9][a-z0-9-]*$" >&2
  echo "Tip: pass --slug my-post-name" >&2
  exit 1
fi

target="content/${section}/${slug}/index.md"

if [ -e "$target" ]; then
  echo "Error: target file already exists: $target" >&2
  exit 1
fi

hugo new "$target" >/dev/null

escaped_title="${title//\\/\\\\}"
escaped_title="${escaped_title//\"/\\\"}"
tmp_file="$(mktemp)"

awk -v title="$escaped_title" -v publish="$publish" '
BEGIN {
  title_done = 0
  draft_done = 0
}
{
  if (!title_done && $0 ~ /^title[[:space:]]*=/) {
    print "title = \"" title "\""
    title_done = 1
    next
  }
  if (publish == 1 && !draft_done && $0 ~ /^draft[[:space:]]*=/) {
    print "draft = false"
    draft_done = 1
    next
  }
  print
}
' "$target" > "$tmp_file"

mv "$tmp_file" "$target"

echo "Created: $target"
echo "Preview: hugo server -D --buildFuture"
