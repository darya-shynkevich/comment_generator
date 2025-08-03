# Comment generator services

- Based on FastAPI Supbase Template
- Generates comment about given words

## Usage

```bash
curl --location 'http://0.0.0.0:8000/api/v1/comments/' \
--header 'Content-Type: application/json' \
--data '{"keywords": ["lovely", "husband"]}'
```

```bash
curl --location 'http://0.0.0.0:8000/api/v1/comments/'
```

## Configuration and launch

This projects uses the following standard tools:
> [uv](https://github.com/astral-sh/uv) is an extremely fast Python package and project manager, written in Rust.

### [Supabase](https://supabase.com/docs/guides/local-development/cli/getting-started?queryGroups=platform&platform=linux&queryGroups=access-method&access-method=postgres)

install supabase-cli

```bash
# brew in linux https://brew.sh/
brew install supabase/tap/supabase
```

launch supabase docker containers

```bash
# under repo root
supabase start
```

### Environment variables

Generate `.env` file based on `example.env` file

### Dependencies installation

```bash
uv sync --all-groups --dev
```

### Migrations

```bash
make migrate
```

```bash
make downgrade
```

```bash
make migrations
```

### Test

```bash
make test
```

### Launch

```bash
make start
```

## Docker

build

```bash
make docker-build
```

test

```bash
make docker-start
```
