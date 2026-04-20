# Anyrow Python SDK

[![MIT License](https://img.shields.io/badge/license-MIT-blue)](./LICENSE)

Python client for the [Anyrow](https://anyrow.ai) API.

## Installation

```bash
pip install anyrow
```

## Quick start

```python
from anyrow import AnyrowSDK

client = AnyrowSDK(
    base_url="https://api.anyrow.ai",
    headers={"Authorization": "Bearer YOUR_API_KEY"},
)

result = client.extract.call(
    params={"project_id": "proj_123"},
    json={"url": "https://example.com/document.pdf"},
)
```

## Resources

- [OpenAPI spec](https://anyrow.ai/openapi.json)
- [TypeScript SDK](https://github.com/anyrow/sdk-typescript)
- [Go SDK](https://github.com/anyrow/sdk-go)
- [CLI](https://github.com/anyrow/cli)

## License

MIT — see [LICENSE](./LICENSE).
