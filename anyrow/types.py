# ruff: noqa: E501
from __future__ import annotations

from typing import Any, Literal, NewType, NotRequired, TypedDict

class CreateOrganizationsWebhookRequest(TypedDict, total=False):
    events: list[Literal["batch.complete", "batch.failed", "batch.partial", "ping"]]
    name: NotRequired[str]
    url: str

class CreateOrganizationsWebhookResponse201(TypedDict, total=False):
    active: bool
    created_at: int
    events_json: list[Literal["batch.complete", "batch.failed", "batch.partial", "ping"]]
    failure_count: int
    id: str
    last_triggered_at: int | None
    name: str | None
    organization_id: str
    secret: str
    secret_rotated_at: int | None
    updated_at: int
    url: str

class CreateOrganizationsWebhooksTestResponse200(TypedDict, total=False):
    http_status: float | None
    response_body: str | None
    status: Literal["error", "success", "timeout"]

class CreateProjectsExtractResponse200(TypedDict, total=False):
    batch_id: NotRequired[str]
    confidence: float | None
    duration_ms: float | None
    fail_count: float
    files: list[TypedDict("X", {"confidence": NotRequired[float | None], "error": NotRequired[Any | None], "file_name": NotRequired[Any | None], "rows": NotRequired[float | None], "status": NotRequired[str]})]
    result: NotRequired[CreateProjectsExtractResponse200Result]
    status: str
    success_count: float
    total_rows: float

CreateProjectsExtractResponse200Result = NewType("CreateProjectsExtractResponse200Result", Any)  # type: ignore[misc]

class CreateProjectsSuggestSchemaResponse200(TypedDict, total=False):
    columns: list[TypedDict("X", {"description": NotRequired[str], "name": str, "type": str})]
    confidence: float
    instruction: NotRequired[str]

class CreateProjectsTableRequest(TypedDict, total=False):
    columns_json: list[TypedDict("X", {"currency_code": NotRequired[str], "default": NotRequired[Any], "description": NotRequired[str | None], "id": str, "instruction": NotRequired[str | None], "name": str, "options": NotRequired[list[str]], "required": NotRequired[bool], "searchable": NotRequired[bool], "type": NotRequired[Literal["array", "boolean", "currency", "date", "email", "enum", "multi_select", "number", "string", "text", "url"]]})]
    default_sort: NotRequired[str]
    insert_mode: NotRequired[Literal["append", "dedup", "merge", "replace"]]
    instruction: NotRequired[str | None]
    merge_columns_json: NotRequired[list[str] | None]
    name: str
    strictness: NotRequired[Literal["strict", "balanced", "flexible"]]

class CreateProjectsTablesColumnRequest(TypedDict, total=False):
    currency_code: NotRequired[str]
    description: NotRequired[str | None]
    instruction: NotRequired[str | None]
    name: str
    options: NotRequired[list[str]]
    required: NotRequired[bool]
    type: NotRequired[Literal["array", "boolean", "currency", "date", "email", "enum", "multi_select", "number", "string", "text", "url"]]

class CreateProjectsTablesDuplicateRequest(TypedDict, total=False):
    name: str
    slug: str

class CreateProjectsTablesRestoreRequest(TypedDict, total=False):
    slug: NotRequired[str]

CreateProjectsTablesRowRequest = NewType("CreateProjectsTablesRowRequest", Any)  # type: ignore[misc]

class CreateProjectsTablesRowRequest_dbbb57(TypedDict, total=False):
    creates: NotRequired[list[dict[str, Any]]]
    deletes: NotRequired[list[str]]
    updates: NotRequired[list[TypedDict("X", {"data": dict[str, Any], "id": str})]]

class CreateProjectsTablesRowResponse200(TypedDict, total=False):
    created: NotRequired[list[dict[str, Any]]]
    deleted: NotRequired[list[str]]
    updated: NotRequired[list[dict[str, Any]]]

class CreateProjectsTableTemplatesUseRequest(TypedDict, total=False):
    name: str
    slug: NotRequired[str]

class CreateProjectsTableTemplatesUseResponse201(TypedDict, total=False):
    columns_json: list[TypedDict("X", {"currency_code": NotRequired[str], "default": NotRequired[Any], "description": NotRequired[str | None], "id": str, "instruction": NotRequired[str | None], "name": str, "options": NotRequired[list[str]], "required": bool, "searchable": NotRequired[bool], "type": Literal["array", "boolean", "currency", "date", "email", "enum", "multi_select", "number", "string", "text", "url"]})]
    created_at: int
    data_version: int
    default_sort: str | None
    deleted_at: int | None
    fts_version: int
    id: str
    insert_mode: Literal["append", "dedup", "merge", "replace"]
    instruction: str | None
    last_used_at: int | None
    merge_columns_json: list[str] | None
    name: str
    project_id: str
    row_count: int
    slug: str
    strictness: Literal["strict", "balanced", "flexible"]
    updated_at: int
    usage_count: int

class CreateTableTemplateRequest(TypedDict, total=False):
    category: str
    columns_json: list[TypedDict("X", {"currency_code": NotRequired[str], "default": NotRequired[Any], "description": NotRequired[str | None], "id": str, "instruction": NotRequired[str | None], "name": str, "options": NotRequired[list[str]], "required": NotRequired[bool], "searchable": NotRequired[bool], "type": NotRequired[Literal["array", "boolean", "currency", "date", "email", "enum", "multi_select", "number", "string", "text", "url"]]})]
    description: NotRequired[str | None]
    insert_mode: NotRequired[Literal["append", "dedup", "merge", "replace"]]
    instruction: NotRequired[str | None]
    merge_columns_json: NotRequired[list[str] | None]
    name: str
    strictness: NotRequired[Literal["strict", "balanced", "flexible"]]

class DeleteOrganizationsWebhookResponse200(TypedDict, total=False):
    id: str

class Err400InvalidInput(TypedDict, total=False):
    error_key: Literal["invalid_input"]
    fields: dict[str, list[TypedDict("X", {"error_key": str, "message": str, "path": str})]]
    message: str
    status: Literal[400]
    status_key: str
    success: Literal[False]

class Err401Unauthorized(TypedDict, total=False):
    error_key: Literal["unauthorized"]
    fields: dict[str, list[TypedDict("X", {"error_key": str, "message": str, "path": str})]]
    message: str
    status: Literal[401]
    status_key: str
    success: Literal[False]

class Err403EmailNotVerifiedForbidden(TypedDict, total=False):
    error_key: Literal["email_not_verified", "forbidden"]
    fields: dict[str, list[TypedDict("X", {"error_key": str, "message": str, "path": str})]]
    message: str
    status: Literal[403]
    status_key: str
    success: Literal[False]

class Err413ContentTooLarge(TypedDict, total=False):
    error_key: Literal["content_too_large"]
    fields: dict[str, list[TypedDict("X", {"error_key": str, "message": str, "path": str})]]
    message: str
    status: Literal[413]
    status_key: str
    success: Literal[False]

class Err415UnsupportedMediaType(TypedDict, total=False):
    error_key: Literal["unsupported_media_type"]
    fields: dict[str, list[TypedDict("X", {"error_key": str, "message": str, "path": str})]]
    message: str
    status: Literal[415]
    status_key: str
    success: Literal[False]

class Err500InternalServerError(TypedDict, total=False):
    error_key: Literal["internal_server_error"]
    fields: dict[str, list[TypedDict("X", {"error_key": str, "message": str, "path": str})]]
    message: str
    status: Literal[500]
    status_key: str
    success: Literal[False]

class GetOrganizationsWebhookResponse200(TypedDict, total=False):
    active: bool
    created_at: int
    events_json: list[Literal["batch.complete", "batch.failed", "batch.partial", "ping"]]
    failure_count: int
    id: str
    last_triggered_at: int | None
    name: str | None
    organization_id: str
    secret_rotated_at: int | None
    updated_at: int
    url: str

class GetProjectsBatcheResponse200(TypedDict, total=False):
    actor_id: str
    actor_type: Literal["user", "api_key"]
    confidence: float | None
    created_at: int
    csv_key: str | None
    current_file: str | None
    duration_ms: int | None
    error: str | None
    extractions: NotRequired[list[TypedDict("X", {"batch_id": str, "confidence": float | None, "created_at": int, "error": str | None, "file_checksum": str | None, "file_key": str, "file_name": str, "file_type": Literal["text_pdf", "scanned", "image", "text", "document", "unknown"] | None, "id": str, "row_count": int | None, "rows_key": str | None, "status": Literal["pending", "processing", "complete", "failed"], "table_id": str | None})]]
    file_count: int
    files_done: int
    id: str
    insert_mode: Literal["append", "dedup", "merge", "replace"] | None
    json_key: str | None
    project_id: str
    schema_json: TypedDict("X", {"columns": list[TypedDict("X", {"description": NotRequired[str | None], "instruction": NotRequired[str | None], "name": str, "type": Literal["array", "boolean", "currency", "date", "email", "enum", "multi_select", "number", "string", "text", "url"]})], "instruction": NotRequired[str | None], "strictness": Literal["strict", "balanced", "flexible"]})
    status: Literal["uploading", "processing", "merging", "complete", "partial", "failed"]
    table_id: str | None
    total_rows: int | None
    updated_at: int
    xlsx_key: str | None

class GetProjectsExportResponse200(TypedDict, total=False):
    actor_id: str
    checksum: str
    created_at: int
    csv_key: str | None
    error: str | None
    expires_at: int | None
    filter_json: str | None
    id: str
    json_key: str | None
    project_id: str
    row_count: int | None
    status: Literal["processing", "complete", "failed"]
    table_id: str | None
    updated_at: int
    xlsx_key: str | None

class GetProjectsTableTemplateResponse200(TypedDict, total=False):
    category: str
    columns_json: list[TypedDict("X", {"currency_code": NotRequired[str], "default": NotRequired[Any], "description": NotRequired[str | None], "id": str, "instruction": NotRequired[str | None], "name": str, "options": NotRequired[list[str]], "required": bool, "searchable": NotRequired[bool], "type": Literal["array", "boolean", "currency", "date", "email", "enum", "multi_select", "number", "string", "text", "url"]})]
    created_at: int
    creator_display_name: str | None
    creator_user_id: str | None
    description: str | None
    id: str
    insert_mode: Literal["append", "dedup", "merge", "replace"]
    instruction: str | None
    merge_columns_json: list[str] | None
    name: str
    strictness: Literal["strict", "balanced", "flexible"]
    updated_at: int
    usage_count: int

class ListOrganizationsWebhooksDeliveriesResponse200(TypedDict, total=False):
    count: int
    deliveries: list[TypedDict("X", {"attempt": int, "created_at": int, "delivered_at": int | None, "event": Literal["batch.complete", "batch.failed", "batch.partial", "ping"], "http_status": int | None, "id": str, "next_retry_at": int | None, "payload_json": str, "response_body": str | None, "status": Literal["pending", "success", "failed"], "webhook_id": str})]
    hasMore: bool
    limit: int
    nextCursor: str | None
    page: int | None

class ListOrganizationsWebhooksResponse200(TypedDict, total=False):
    count: int
    hasMore: bool
    limit: int
    nextCursor: str | None
    page: int | None
    webhooks: list[TypedDict("X", {"active": bool, "created_at": int, "events_json": list[Literal["batch.complete", "batch.failed", "batch.partial", "ping"]], "failure_count": int, "id": str, "last_triggered_at": int | None, "name": str | None, "organization_id": str, "secret_rotated_at": int | None, "updated_at": int, "url": str})]

class ListProjectsBatchesResponse200(TypedDict, total=False):
    batches: list[TypedDict("X", {"actor_id": str, "actor_type": Literal["user", "api_key"], "confidence": float | None, "created_at": int, "csv_key": str | None, "current_file": str | None, "duration_ms": int | None, "error": str | None, "file_count": int, "files_done": int, "id": str, "insert_mode": Literal["append", "dedup", "merge", "replace"] | None, "json_key": str | None, "project_id": str, "schema_json": TypedDict("X", {"columns": list[TypedDict("X", {"description": NotRequired[str | None], "instruction": NotRequired[str | None], "name": str, "type": Literal["array", "boolean", "currency", "date", "email", "enum", "multi_select", "number", "string", "text", "url"]})], "instruction": NotRequired[str | None], "strictness": Literal["strict", "balanced", "flexible"]}), "status": Literal["uploading", "processing", "merging", "complete", "partial", "failed"], "table_id": str | None, "total_rows": int | None, "updated_at": int, "xlsx_key": str | None})]
    count: int
    hasMore: bool
    limit: int
    nextCursor: str | None
    page: int | None

class ListProjectsTablesColumnsDistinctResponse200(TypedDict, total=False):
    values: list[str | float | None]

class ListProjectsTablesResponse200(TypedDict, total=False):
    count: int
    hasMore: bool
    limit: int
    nextCursor: str | None
    page: int | None
    tables: list[TypedDict("X", {"columns_json": list[TypedDict("X", {"currency_code": NotRequired[str], "default": NotRequired[Any], "description": NotRequired[str | None], "id": str, "instruction": NotRequired[str | None], "name": str, "options": NotRequired[list[str]], "required": bool, "searchable": NotRequired[bool], "type": Literal["array", "boolean", "currency", "date", "email", "enum", "multi_select", "number", "string", "text", "url"]})], "created_at": int, "data_version": int, "default_sort": str | None, "deleted_at": int | None, "fts_version": int, "id": str, "insert_mode": Literal["append", "dedup", "merge", "replace"], "instruction": str | None, "last_used_at": int | None, "merge_columns_json": list[str] | None, "name": str, "project_id": str, "row_count": int, "slug": str, "strictness": Literal["strict", "balanced", "flexible"], "updated_at": int, "usage_count": int})]

class ListProjectsTablesRowsResponse200(TypedDict, total=False):
    count: int
    hasMore: bool
    limit: int
    nextCursor: str | None
    page: int | None
    rows: list[dict[str, Any]]

ListProjectsTablesRowsResponse200_f7f633 = NewType("ListProjectsTablesRowsResponse200_f7f633", Any)  # type: ignore[misc]

class ListProjectsTableTemplatesResponse200(TypedDict, total=False):
    count: int
    hasMore: bool
    limit: int
    nextCursor: str | None
    page: int | None
    templates: list[TypedDict("X", {"category": str, "columns_json": list[TypedDict("X", {"currency_code": NotRequired[str], "default": NotRequired[Any], "description": NotRequired[str | None], "id": str, "instruction": NotRequired[str | None], "name": str, "options": NotRequired[list[str]], "required": bool, "searchable": NotRequired[bool], "type": Literal["array", "boolean", "currency", "date", "email", "enum", "multi_select", "number", "string", "text", "url"]})], "created_at": int, "creator_display_name": str | None, "creator_user_id": str | None, "description": str | None, "id": str, "insert_mode": Literal["append", "dedup", "merge", "replace"], "instruction": str | None, "merge_columns_json": list[str] | None, "name": str, "strictness": Literal["strict", "balanced", "flexible"], "updated_at": int, "usage_count": int})]

class ReplaceProjectsTablesColumnRequest(TypedDict, total=False):
    order: list[str]

class UpdateOrganizationsWebhookRequest(TypedDict, total=False):
    active: NotRequired[bool]
    events: NotRequired[list[Literal["batch.complete", "batch.failed", "batch.partial", "ping"]]]
    name: NotRequired[str]
    url: NotRequired[str]

class UpdateProjectsTableRequest(TypedDict, total=False):
    default_sort: NotRequired[str | None]
    insert_mode: NotRequired[Literal["append", "dedup", "merge", "replace"]]
    instruction: NotRequired[str | None]
    merge_columns_json: NotRequired[list[str] | None]
    name: NotRequired[str]
    slug: NotRequired[str]
    strictness: NotRequired[Literal["strict", "balanced", "flexible"]]

class UpdateProjectsTablesColumnRequest(TypedDict, total=False):
    description: NotRequired[str | None]
    instruction: NotRequired[str | None]
    name: NotRequired[str]
    options: NotRequired[list[str]]
    required: NotRequired[bool]
    searchable: NotRequired[bool]
    type: NotRequired[Literal["array", "boolean", "currency", "date", "email", "enum", "multi_select", "number", "string", "text", "url"]]

class UpdateTableTemplateRequest(TypedDict, total=False):
    category: NotRequired[str]
    columns_json: NotRequired[list[TypedDict("X", {"currency_code": NotRequired[str], "default": NotRequired[Any], "description": NotRequired[str | None], "id": str, "instruction": NotRequired[str | None], "name": str, "options": NotRequired[list[str]], "required": NotRequired[bool], "searchable": NotRequired[bool], "type": NotRequired[Literal["array", "boolean", "currency", "date", "email", "enum", "multi_select", "number", "string", "text", "url"]]})]]
    description: NotRequired[str | None]
    insert_mode: NotRequired[Literal["append", "dedup", "merge", "replace"]]
    instruction: NotRequired[str | None]
    merge_columns_json: NotRequired[list[str] | None]
    name: NotRequired[str]
    strictness: NotRequired[Literal["strict", "balanced", "flexible"]]

__all__ = ["CreateOrganizationsWebhookRequest", "CreateOrganizationsWebhookResponse201", "CreateOrganizationsWebhooksTestResponse200", "CreateProjectsExtractResponse200", "CreateProjectsExtractResponse200Result", "CreateProjectsSuggestSchemaResponse200", "CreateProjectsTableRequest", "CreateProjectsTablesColumnRequest", "CreateProjectsTablesDuplicateRequest", "CreateProjectsTablesRestoreRequest", "CreateProjectsTablesRowRequest", "CreateProjectsTablesRowRequest_dbbb57", "CreateProjectsTablesRowResponse200", "CreateProjectsTableTemplatesUseRequest", "CreateProjectsTableTemplatesUseResponse201", "CreateTableTemplateRequest", "DeleteOrganizationsWebhookResponse200", "Err400InvalidInput", "Err401Unauthorized", "Err403EmailNotVerifiedForbidden", "Err413ContentTooLarge", "Err415UnsupportedMediaType", "Err500InternalServerError", "GetOrganizationsWebhookResponse200", "GetProjectsBatcheResponse200", "GetProjectsExportResponse200", "GetProjectsTableTemplateResponse200", "ListOrganizationsWebhooksDeliveriesResponse200", "ListOrganizationsWebhooksResponse200", "ListProjectsBatchesResponse200", "ListProjectsTablesColumnsDistinctResponse200", "ListProjectsTablesResponse200", "ListProjectsTablesRowsResponse200", "ListProjectsTablesRowsResponse200_f7f633", "ListProjectsTableTemplatesResponse200", "ReplaceProjectsTablesColumnRequest", "UpdateOrganizationsWebhookRequest", "UpdateProjectsTableRequest", "UpdateProjectsTablesColumnRequest", "UpdateTableTemplateRequest"]