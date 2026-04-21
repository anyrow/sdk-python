# ruff: noqa: E501
from __future__ import annotations

import threading
import httpx
from urllib.parse import quote
from typing import Any, Literal
from ._runtime import (
    ClientConfig,
    _build_headers,
    _build_url,
    _do_request_async,
    _do_request_sync,
    _parse_body,
    _raise_for_status,
)
from ._invalidation import _StaleTracker, _StaleTrackerSync, interpolate_path
from .types import (
    CreateOrganizationsWebhookRequest,
    CreateOrganizationsWebhookResponse201,
    ListOrganizationsWebhooksResponse200,
    GetOrganizationsWebhookResponse200,
    UpdateOrganizationsWebhookRequest,
    DeleteOrganizationsWebhookResponse200,
    ListOrganizationsWebhooksDeliveriesResponse200,
    CreateOrganizationsWebhooksTestResponse200,
    ListProjectsBatchesResponse200,
    GetProjectsBatcheResponse200,
    GetProjectsExportResponse200,
    CreateProjectsExtractResponse200,
    CreateProjectsSuggestSchemaResponse200,
    ListProjectsTableTemplatesResponse200,
    GetProjectsTableTemplateResponse200,
    CreateProjectsTableTemplatesUseRequest,
    CreateProjectsTableTemplatesUseResponse201,
    ListProjectsTablesResponse200,
    CreateProjectsTableRequest,
    UpdateProjectsTableRequest,
    CreateProjectsTablesColumnRequest,
    ReplaceProjectsTablesColumnRequest,
    UpdateProjectsTablesColumnRequest,
    ListProjectsTablesColumnsDistinctResponse200,
    CreateProjectsTablesDuplicateRequest,
    CreateProjectsTablesRestoreRequest,
    ListProjectsTablesRowsResponse200,
    CreateProjectsTablesRowRequest,
    ListProjectsTablesRowsResponse200_f7f633,
    CreateProjectsTablesRowRequest_dbbb57,
    CreateProjectsTablesRowResponse200,
    CreateTableTemplateRequest,
    UpdateTableTemplateRequest,
)

_INVALIDATION_MAP: dict[str, dict[str, Any]] = {
}

class _BatchDownloadResource:
    def __init__(self, _client: _BatchResource) -> None:
        self._client = _client

    async def csv(self, project_id: str, batch_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> None:
        """Download batch CSV

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/batches/{quote(batch_id, safe='')}/download/csv")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "batch_id": batch_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/batches/{batch_id}/download/csv", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/batches/{batch_id}/download/csv",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def json(self, project_id: str, batch_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> None:
        """Download batch JSON

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/batches/{quote(batch_id, safe='')}/download/json")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "batch_id": batch_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/batches/{batch_id}/download/json", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/batches/{batch_id}/download/json",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def xlsx(self, project_id: str, batch_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> None:
        """Download batch XLSX

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/batches/{quote(batch_id, safe='')}/download/xlsx")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "batch_id": batch_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/batches/{batch_id}/download/xlsx", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/batches/{batch_id}/download/xlsx",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)


class _BatchResource:
    def __init__(self, _client: "AsyncSDK") -> None:
        self._client = _client
        self.download = _BatchDownloadResource(self)

    async def get(self, project_id: str, batch_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> GetProjectsBatcheResponse200:
        """Get batch

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/batches/{quote(batch_id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "batch_id": batch_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/batches/{batch_id}", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/batches/{batch_id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def list(self, project_id: str,
        *,
        cursor: str | None = None,
        filter: str | None = None,
        lang: str | None = None,
        order: str | None = None,
        page: int | None = None,
        q: str | None = None,
        select: str | None = None,
        limit: int | None = None,
        status: Literal["uploading", "processing", "merging", "complete", "partial", "failed"] | None = None,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> ListProjectsBatchesResponse200:
        """List batches

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/batches")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {"cursor": cursor, "filter": filter, "lang": lang, "order": order, "page": page, "q": q, "select": select, "limit": limit, "status": status}
        _path_params: dict[str, str] | None = {"project_id": project_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/batches", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/batches",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)


class _ColumnResource:
    def __init__(self, _client: "AsyncSDK") -> None:
        self._client = _client

    async def add(self, project_id: str, table_id: str, body: CreateProjectsTablesColumnRequest,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsTableTemplatesUseResponse201:
        """Add column

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/columns")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/columns", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "POST", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/projects/{project_id}/tables/{table_id}/columns",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def distinct(self, project_id: str, table_id: str, col_id: str,
        *,
        limit: int | None = None,
        q: str | None = None,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> ListProjectsTablesColumnsDistinctResponse200:
        """Get distinct column values

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/columns/{quote(col_id, safe='')}/distinct")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {"limit": limit, "q": q}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id, "col_id": col_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/columns/{col_id}/distinct", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/tables/{table_id}/columns/{col_id}/distinct",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def remove(self, project_id: str, table_id: str, col_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsTableTemplatesUseResponse201:
        """Remove column

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/columns/{quote(col_id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id, "col_id": col_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/columns/{col_id}", _path_params)
        _concrete_selector = "DELETE " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "DELETE",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "DELETE", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="DELETE /v1/projects/{project_id}/tables/{table_id}/columns/{col_id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "DELETE",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def reorder(self, project_id: str, table_id: str, body: ReplaceProjectsTablesColumnRequest,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsTableTemplatesUseResponse201:
        """Reorder columns

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/columns/order")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/columns/order", _path_params)
        _concrete_selector = "PUT " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "PUT",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "PUT", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="PUT /v1/projects/{project_id}/tables/{table_id}/columns/order",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "PUT",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def update(self, project_id: str, table_id: str, col_id: str, body: UpdateProjectsTablesColumnRequest,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsTableTemplatesUseResponse201:
        """Update column

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/columns/{quote(col_id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id, "col_id": col_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/columns/{col_id}", _path_params)
        _concrete_selector = "PATCH " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "PATCH",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "PATCH", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="PATCH /v1/projects/{project_id}/tables/{table_id}/columns/{col_id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "PATCH",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)


class _ExportResource:
    def __init__(self, _client: "AsyncSDK") -> None:
        self._client = _client

    async def get(self, project_id: str, export_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> GetProjectsExportResponse200:
        """Get export status

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/exports/{quote(export_id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "export_id": export_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/exports/{export_id}", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/exports/{export_id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)


class _ExtractTableResource:
    def __init__(self, _client: _ExtractResource) -> None:
        self._client = _client

    async def once(self, project_id: str, table_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsExtractResponse200:
        """Extract into table (JSON response)

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/extract")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/extract", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "POST", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/projects/{project_id}/tables/{table_id}/extract",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def stream(self, project_id: str, table_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> None:
        """Extract into table (SSE stream)

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/extract-stream")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/extract-stream", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "POST", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/projects/{project_id}/tables/{table_id}/extract-stream",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)


class _ExtractResource:
    def __init__(self, _client: "AsyncSDK") -> None:
        self._client = _client
        self.table = _ExtractTableResource(self)

    async def once(self, project_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsExtractResponse200:
        """Extract data from text or file (JSON response)

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/extract")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/extract", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "POST", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/projects/{project_id}/extract",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def stream(self, project_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> None:
        """Extract data from text or file (SSE stream)

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/extract-stream")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/extract-stream", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "POST", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/projects/{project_id}/extract-stream",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)


class _RowResource:
    def __init__(self, _client: "AsyncSDK") -> None:
        self._client = _client

    async def aggregate(self, project_id: str, table_id: str, aggs: str,
        *,
        filter: str | None = None,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> ListProjectsTablesRowsResponse200_f7f633:
        """Aggregate column values

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/rows/aggregate")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {"aggs": aggs, "filter": filter}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/rows/aggregate", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/tables/{table_id}/rows/aggregate",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def bulk(self, project_id: str, table_id: str, body: CreateProjectsTablesRowRequest_dbbb57,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsTablesRowResponse200:
        """Bulk create/update/delete rows

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/rows/bulk")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/rows/bulk", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "POST", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/projects/{project_id}/tables/{table_id}/rows/bulk",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def create(self, project_id: str, table_id: str, body: CreateProjectsTablesRowRequest,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsTablesRowRequest:
        """Create row

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/rows")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/rows", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "POST", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/projects/{project_id}/tables/{table_id}/rows",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def delete(self, project_id: str, table_id: str, row_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> DeleteOrganizationsWebhookResponse200:
        """Delete row

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/rows/{quote(row_id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id, "row_id": row_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/rows/{row_id}", _path_params)
        _concrete_selector = "DELETE " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "DELETE",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "DELETE", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="DELETE /v1/projects/{project_id}/tables/{table_id}/rows/{row_id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "DELETE",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def get(self, project_id: str, table_id: str, row_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsTablesRowRequest:
        """Get row

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/rows/{quote(row_id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id, "row_id": row_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/rows/{row_id}", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/tables/{table_id}/rows/{row_id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def list(self, project_id: str, table_id: str,
        *,
        cursor: str | None = None,
        filter: str | None = None,
        limit: int | None = None,
        order: str | None = None,
        page: int | None = None,
        q: str | None = None,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> ListProjectsTablesRowsResponse200:
        """List rows

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/rows")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {"cursor": cursor, "filter": filter, "limit": limit, "order": order, "page": page, "q": q}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/rows", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/tables/{table_id}/rows",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def update(self, project_id: str, table_id: str, row_id: str, body: CreateProjectsTablesRowRequest,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsTablesRowRequest:
        """Update row

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/rows/{quote(row_id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id, "row_id": row_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/rows/{row_id}", _path_params)
        _concrete_selector = "PATCH " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "PATCH",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "PATCH", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="PATCH /v1/projects/{project_id}/tables/{table_id}/rows/{row_id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "PATCH",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)


class _SuggestResource:
    def __init__(self, _client: "AsyncSDK") -> None:
        self._client = _client

    async def schema(self, project_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsSuggestSchemaResponse200:
        """Suggest schema from text or file (multipart)

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/suggest-schema")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/suggest-schema", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "POST", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/projects/{project_id}/suggest-schema",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)


class _TableResource:
    def __init__(self, _client: "AsyncSDK") -> None:
        self._client = _client

    async def create(self, project_id: str, body: CreateProjectsTableRequest,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsTableTemplatesUseResponse201:
        """Create table

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "POST", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/projects/{project_id}/tables",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def delete(self, project_id: str, table_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> DeleteOrganizationsWebhookResponse200:
        """Delete table (soft, 72h grace)

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}", _path_params)
        _concrete_selector = "DELETE " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "DELETE",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "DELETE", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="DELETE /v1/projects/{project_id}/tables/{table_id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "DELETE",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def duplicate(self, project_id: str, table_id: str, body: CreateProjectsTablesDuplicateRequest,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsTableTemplatesUseResponse201:
        """Duplicate table structure

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/duplicate")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/duplicate", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "POST", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/projects/{project_id}/tables/{table_id}/duplicate",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def export(self, project_id: str, table_id: str, format: Literal["csv", "json", "xlsx"],
        *,
        filter: str | None = None,
        order: str | None = None,
        schema: Literal["true", "false"] | None = None,
        search: str | None = None,
        since: str | None = None,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> GetProjectsExportResponse200:
        """Export table rows

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/export")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {"filter": filter, "format": format, "order": order, "schema": schema, "search": search, "since": since}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/export", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/tables/{table_id}/export",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def get(self, project_id: str, table_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsTableTemplatesUseResponse201:
        """Get table

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/tables/{table_id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def list(self, project_id: str,
        *,
        cursor: str | None = None,
        filter: str | None = None,
        lang: str | None = None,
        order: str | None = None,
        page: int | None = None,
        q: str | None = None,
        select: str | None = None,
        limit: int | None = None,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> ListProjectsTablesResponse200:
        """List tables

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {"cursor": cursor, "filter": filter, "lang": lang, "order": order, "page": page, "q": q, "select": select, "limit": limit}
        _path_params: dict[str, str] | None = {"project_id": project_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/tables",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def restore(self, project_id: str, table_id: str, body: CreateProjectsTablesRestoreRequest,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsTableTemplatesUseResponse201:
        """Restore deleted table

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/restore")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/restore", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "POST", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/projects/{project_id}/tables/{table_id}/restore",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def update(self, project_id: str, table_id: str, body: UpdateProjectsTableRequest,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsTableTemplatesUseResponse201:
        """Update table

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}", _path_params)
        _concrete_selector = "PATCH " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "PATCH",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "PATCH", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="PATCH /v1/projects/{project_id}/tables/{table_id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "PATCH",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)


class _TableTemplateResource:
    def __init__(self, _client: "AsyncSDK") -> None:
        self._client = _client

    async def create(self, body: CreateTableTemplateRequest,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> GetProjectsTableTemplateResponse200:
        """Create table template

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, "/v1/table-templates")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = None
        _concrete_path = interpolate_path("/v1/table-templates", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "POST", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/table-templates",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def delete(self, template_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> DeleteOrganizationsWebhookResponse200:
        """Delete table template

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/table-templates/{quote(template_id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"template_id": template_id}
        _concrete_path = interpolate_path("/v1/table-templates/{template_id}", _path_params)
        _concrete_selector = "DELETE " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "DELETE",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "DELETE", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="DELETE /v1/table-templates/{template_id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "DELETE",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def list_mine(self,
        *,
        cursor: str | None = None,
        filter: str | None = None,
        lang: str | None = None,
        order: str | None = None,
        page: int | None = None,
        q: str | None = None,
        select: str | None = None,
        limit: int | None = None,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> ListProjectsTableTemplatesResponse200:
        """List my table templates

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, "/v1/table-templates/mine")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {"cursor": cursor, "filter": filter, "lang": lang, "order": order, "page": page, "q": q, "select": select, "limit": limit}
        _path_params: dict[str, str] | None = None
        _concrete_path = interpolate_path("/v1/table-templates/mine", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/table-templates/mine",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def project_get(self, project_id: str, template_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> GetProjectsTableTemplateResponse200:
        """Preview table template

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/table-templates/{quote(template_id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "template_id": template_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/table-templates/{template_id}", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/table-templates/{template_id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def project_list(self, project_id: str,
        *,
        cursor: str | None = None,
        filter: str | None = None,
        lang: str | None = None,
        order: str | None = None,
        page: int | None = None,
        q: str | None = None,
        select: str | None = None,
        limit: int | None = None,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> ListProjectsTableTemplatesResponse200:
        """Browse table templates

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/table-templates")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {"cursor": cursor, "filter": filter, "lang": lang, "order": order, "page": page, "q": q, "select": select, "limit": limit}
        _path_params: dict[str, str] | None = {"project_id": project_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/table-templates", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/table-templates",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def update(self, template_id: str, body: UpdateTableTemplateRequest,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> GetProjectsTableTemplateResponse200:
        """Update table template

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/table-templates/{quote(template_id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"template_id": template_id}
        _concrete_path = interpolate_path("/v1/table-templates/{template_id}", _path_params)
        _concrete_selector = "PATCH " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "PATCH",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "PATCH", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="PATCH /v1/table-templates/{template_id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "PATCH",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def use(self, project_id: str, template_id: str, body: CreateProjectsTableTemplatesUseRequest,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsTableTemplatesUseResponse201:
        """Create table from template

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/table-templates/{quote(template_id, safe='')}/use")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "template_id": template_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/table-templates/{template_id}/use", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "POST", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/projects/{project_id}/table-templates/{template_id}/use",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)


class _WebhookResource:
    def __init__(self, _client: "AsyncSDK") -> None:
        self._client = _client

    async def create(self, organization_id: str, body: CreateOrganizationsWebhookRequest,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateOrganizationsWebhookResponse201:
        """Create webhook

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/organizations/{quote(organization_id, safe='')}/webhooks")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"organization_id": organization_id}
        _concrete_path = interpolate_path("/v1/organizations/{organization_id}/webhooks", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "POST", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/organizations/{organization_id}/webhooks",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def delete(self, organization_id: str, id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> DeleteOrganizationsWebhookResponse200:
        """Delete webhook

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/organizations/{quote(organization_id, safe='')}/webhooks/{quote(id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"organization_id": organization_id, "id": id}
        _concrete_path = interpolate_path("/v1/organizations/{organization_id}/webhooks/{id}", _path_params)
        _concrete_selector = "DELETE " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "DELETE",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "DELETE", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="DELETE /v1/organizations/{organization_id}/webhooks/{id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "DELETE",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def deliveries(self, organization_id: str, id: str,
        *,
        cursor: str | None = None,
        filter: str | None = None,
        lang: str | None = None,
        order: str | None = None,
        page: int | None = None,
        q: str | None = None,
        select: str | None = None,
        limit: int | None = None,
        event: Literal["batch.complete", "batch.failed", "batch.partial", "ping"] | None = None,
        status: Literal["pending", "success", "failed"] | None = None,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> ListOrganizationsWebhooksDeliveriesResponse200:
        """List webhook deliveries

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/organizations/{quote(organization_id, safe='')}/webhooks/{quote(id, safe='')}/deliveries")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {"cursor": cursor, "filter": filter, "lang": lang, "order": order, "page": page, "q": q, "select": select, "limit": limit, "event": event, "status": status}
        _path_params: dict[str, str] | None = {"organization_id": organization_id, "id": id}
        _concrete_path = interpolate_path("/v1/organizations/{organization_id}/webhooks/{id}/deliveries", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/organizations/{organization_id}/webhooks/{id}/deliveries",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def get(self, organization_id: str, id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> GetOrganizationsWebhookResponse200:
        """Get webhook

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/organizations/{quote(organization_id, safe='')}/webhooks/{quote(id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"organization_id": organization_id, "id": id}
        _concrete_path = interpolate_path("/v1/organizations/{organization_id}/webhooks/{id}", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/organizations/{organization_id}/webhooks/{id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def list(self, organization_id: str,
        *,
        cursor: str | None = None,
        filter: str | None = None,
        lang: str | None = None,
        order: str | None = None,
        page: int | None = None,
        q: str | None = None,
        select: str | None = None,
        limit: int | None = None,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> ListOrganizationsWebhooksResponse200:
        """List webhooks

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/organizations/{quote(organization_id, safe='')}/webhooks")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {"cursor": cursor, "filter": filter, "lang": lang, "order": order, "page": page, "q": q, "select": select, "limit": limit}
        _path_params: dict[str, str] | None = {"organization_id": organization_id}
        _concrete_path = interpolate_path("/v1/organizations/{organization_id}/webhooks", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/organizations/{organization_id}/webhooks",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def rotate_secret(self, organization_id: str, id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateOrganizationsWebhookResponse201:
        """Rotate webhook secret

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/organizations/{quote(organization_id, safe='')}/webhooks/{quote(id, safe='')}/rotate-secret")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"organization_id": organization_id, "id": id}
        _concrete_path = interpolate_path("/v1/organizations/{organization_id}/webhooks/{id}/rotate-secret", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "POST", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/organizations/{organization_id}/webhooks/{id}/rotate-secret",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def test(self, organization_id: str, id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateOrganizationsWebhooksTestResponse200:
        """Send test webhook

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/organizations/{quote(organization_id, safe='')}/webhooks/{quote(id, safe='')}/test")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"organization_id": organization_id, "id": id}
        _concrete_path = interpolate_path("/v1/organizations/{organization_id}/webhooks/{id}/test", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "POST", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/organizations/{organization_id}/webhooks/{id}/test",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    async def update(self, organization_id: str, id: str, body: UpdateOrganizationsWebhookRequest,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> GetOrganizationsWebhookResponse200:
        """Update webhook

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/organizations/{quote(organization_id, safe='')}/webhooks/{quote(id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"organization_id": organization_id, "id": id}
        _concrete_path = interpolate_path("/v1/organizations/{organization_id}/webhooks/{id}", _path_params)
        _concrete_selector = "PATCH " + _concrete_path
        _request_meta = await self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "PATCH",
        )
        _response = await _do_request_async(
            self._client._async_client, self._client._config, "PATCH", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="PATCH /v1/organizations/{organization_id}/webhooks/{id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            await self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                await self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "PATCH",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)


class _SyncBatchDownloadResource:
    def __init__(self, _client: _SyncBatchResource) -> None:
        self._client = _client

    def csv(self, project_id: str, batch_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> None:
        """Download batch CSV

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/batches/{quote(batch_id, safe='')}/download/csv")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "batch_id": batch_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/batches/{batch_id}/download/csv", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/batches/{batch_id}/download/csv",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def json(self, project_id: str, batch_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> None:
        """Download batch JSON

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/batches/{quote(batch_id, safe='')}/download/json")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "batch_id": batch_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/batches/{batch_id}/download/json", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/batches/{batch_id}/download/json",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def xlsx(self, project_id: str, batch_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> None:
        """Download batch XLSX

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/batches/{quote(batch_id, safe='')}/download/xlsx")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "batch_id": batch_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/batches/{batch_id}/download/xlsx", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/batches/{batch_id}/download/xlsx",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)


class _SyncBatchResource:
    def __init__(self, _client: "SDK") -> None:
        self._client = _client
        self.download = _SyncBatchDownloadResource(self)

    def get(self, project_id: str, batch_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> GetProjectsBatcheResponse200:
        """Get batch

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/batches/{quote(batch_id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "batch_id": batch_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/batches/{batch_id}", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/batches/{batch_id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def list(self, project_id: str,
        *,
        cursor: str | None = None,
        filter: str | None = None,
        lang: str | None = None,
        order: str | None = None,
        page: int | None = None,
        q: str | None = None,
        select: str | None = None,
        limit: int | None = None,
        status: Literal["uploading", "processing", "merging", "complete", "partial", "failed"] | None = None,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> ListProjectsBatchesResponse200:
        """List batches

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/batches")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {"cursor": cursor, "filter": filter, "lang": lang, "order": order, "page": page, "q": q, "select": select, "limit": limit, "status": status}
        _path_params: dict[str, str] | None = {"project_id": project_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/batches", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/batches",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)


class _SyncColumnResource:
    def __init__(self, _client: "SDK") -> None:
        self._client = _client

    def add(self, project_id: str, table_id: str, body: CreateProjectsTablesColumnRequest,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsTableTemplatesUseResponse201:
        """Add column

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/columns")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/columns", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "POST", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/projects/{project_id}/tables/{table_id}/columns",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def distinct(self, project_id: str, table_id: str, col_id: str,
        *,
        limit: int | None = None,
        q: str | None = None,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> ListProjectsTablesColumnsDistinctResponse200:
        """Get distinct column values

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/columns/{quote(col_id, safe='')}/distinct")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {"limit": limit, "q": q}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id, "col_id": col_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/columns/{col_id}/distinct", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/tables/{table_id}/columns/{col_id}/distinct",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def remove(self, project_id: str, table_id: str, col_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsTableTemplatesUseResponse201:
        """Remove column

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/columns/{quote(col_id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id, "col_id": col_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/columns/{col_id}", _path_params)
        _concrete_selector = "DELETE " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "DELETE",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "DELETE", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="DELETE /v1/projects/{project_id}/tables/{table_id}/columns/{col_id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "DELETE",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def reorder(self, project_id: str, table_id: str, body: ReplaceProjectsTablesColumnRequest,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsTableTemplatesUseResponse201:
        """Reorder columns

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/columns/order")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/columns/order", _path_params)
        _concrete_selector = "PUT " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "PUT",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "PUT", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="PUT /v1/projects/{project_id}/tables/{table_id}/columns/order",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "PUT",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def update(self, project_id: str, table_id: str, col_id: str, body: UpdateProjectsTablesColumnRequest,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsTableTemplatesUseResponse201:
        """Update column

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/columns/{quote(col_id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id, "col_id": col_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/columns/{col_id}", _path_params)
        _concrete_selector = "PATCH " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "PATCH",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "PATCH", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="PATCH /v1/projects/{project_id}/tables/{table_id}/columns/{col_id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "PATCH",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)


class _SyncExportResource:
    def __init__(self, _client: "SDK") -> None:
        self._client = _client

    def get(self, project_id: str, export_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> GetProjectsExportResponse200:
        """Get export status

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/exports/{quote(export_id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "export_id": export_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/exports/{export_id}", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/exports/{export_id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)


class _SyncExtractTableResource:
    def __init__(self, _client: _SyncExtractResource) -> None:
        self._client = _client

    def once(self, project_id: str, table_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsExtractResponse200:
        """Extract into table (JSON response)

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/extract")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/extract", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "POST", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/projects/{project_id}/tables/{table_id}/extract",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def stream(self, project_id: str, table_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> None:
        """Extract into table (SSE stream)

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/extract-stream")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/extract-stream", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "POST", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/projects/{project_id}/tables/{table_id}/extract-stream",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)


class _SyncExtractResource:
    def __init__(self, _client: "SDK") -> None:
        self._client = _client
        self.table = _SyncExtractTableResource(self)

    def once(self, project_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsExtractResponse200:
        """Extract data from text or file (JSON response)

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/extract")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/extract", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "POST", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/projects/{project_id}/extract",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def stream(self, project_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> None:
        """Extract data from text or file (SSE stream)

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/extract-stream")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/extract-stream", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "POST", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/projects/{project_id}/extract-stream",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)


class _SyncRowResource:
    def __init__(self, _client: "SDK") -> None:
        self._client = _client

    def aggregate(self, project_id: str, table_id: str, aggs: str,
        *,
        filter: str | None = None,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> ListProjectsTablesRowsResponse200_f7f633:
        """Aggregate column values

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/rows/aggregate")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {"aggs": aggs, "filter": filter}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/rows/aggregate", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/tables/{table_id}/rows/aggregate",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def bulk(self, project_id: str, table_id: str, body: CreateProjectsTablesRowRequest_dbbb57,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsTablesRowResponse200:
        """Bulk create/update/delete rows

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/rows/bulk")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/rows/bulk", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "POST", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/projects/{project_id}/tables/{table_id}/rows/bulk",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def create(self, project_id: str, table_id: str, body: CreateProjectsTablesRowRequest,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsTablesRowRequest:
        """Create row

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/rows")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/rows", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "POST", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/projects/{project_id}/tables/{table_id}/rows",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def delete(self, project_id: str, table_id: str, row_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> DeleteOrganizationsWebhookResponse200:
        """Delete row

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/rows/{quote(row_id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id, "row_id": row_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/rows/{row_id}", _path_params)
        _concrete_selector = "DELETE " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "DELETE",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "DELETE", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="DELETE /v1/projects/{project_id}/tables/{table_id}/rows/{row_id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "DELETE",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def get(self, project_id: str, table_id: str, row_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsTablesRowRequest:
        """Get row

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/rows/{quote(row_id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id, "row_id": row_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/rows/{row_id}", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/tables/{table_id}/rows/{row_id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def list(self, project_id: str, table_id: str,
        *,
        cursor: str | None = None,
        filter: str | None = None,
        limit: int | None = None,
        order: str | None = None,
        page: int | None = None,
        q: str | None = None,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> ListProjectsTablesRowsResponse200:
        """List rows

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/rows")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {"cursor": cursor, "filter": filter, "limit": limit, "order": order, "page": page, "q": q}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/rows", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/tables/{table_id}/rows",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def update(self, project_id: str, table_id: str, row_id: str, body: CreateProjectsTablesRowRequest,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsTablesRowRequest:
        """Update row

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/rows/{quote(row_id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id, "row_id": row_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/rows/{row_id}", _path_params)
        _concrete_selector = "PATCH " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "PATCH",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "PATCH", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="PATCH /v1/projects/{project_id}/tables/{table_id}/rows/{row_id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "PATCH",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)


class _SyncSuggestResource:
    def __init__(self, _client: "SDK") -> None:
        self._client = _client

    def schema(self, project_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsSuggestSchemaResponse200:
        """Suggest schema from text or file (multipart)

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/suggest-schema")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/suggest-schema", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "POST", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/projects/{project_id}/suggest-schema",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)


class _SyncTableResource:
    def __init__(self, _client: "SDK") -> None:
        self._client = _client

    def create(self, project_id: str, body: CreateProjectsTableRequest,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsTableTemplatesUseResponse201:
        """Create table

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "POST", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/projects/{project_id}/tables",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def delete(self, project_id: str, table_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> DeleteOrganizationsWebhookResponse200:
        """Delete table (soft, 72h grace)

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}", _path_params)
        _concrete_selector = "DELETE " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "DELETE",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "DELETE", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="DELETE /v1/projects/{project_id}/tables/{table_id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "DELETE",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def duplicate(self, project_id: str, table_id: str, body: CreateProjectsTablesDuplicateRequest,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsTableTemplatesUseResponse201:
        """Duplicate table structure

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/duplicate")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/duplicate", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "POST", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/projects/{project_id}/tables/{table_id}/duplicate",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def export(self, project_id: str, table_id: str, format: Literal["csv", "json", "xlsx"],
        *,
        filter: str | None = None,
        order: str | None = None,
        schema: Literal["true", "false"] | None = None,
        search: str | None = None,
        since: str | None = None,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> GetProjectsExportResponse200:
        """Export table rows

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/export")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {"filter": filter, "format": format, "order": order, "schema": schema, "search": search, "since": since}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/export", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/tables/{table_id}/export",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def get(self, project_id: str, table_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsTableTemplatesUseResponse201:
        """Get table

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/tables/{table_id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def list(self, project_id: str,
        *,
        cursor: str | None = None,
        filter: str | None = None,
        lang: str | None = None,
        order: str | None = None,
        page: int | None = None,
        q: str | None = None,
        select: str | None = None,
        limit: int | None = None,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> ListProjectsTablesResponse200:
        """List tables

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {"cursor": cursor, "filter": filter, "lang": lang, "order": order, "page": page, "q": q, "select": select, "limit": limit}
        _path_params: dict[str, str] | None = {"project_id": project_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/tables",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def restore(self, project_id: str, table_id: str, body: CreateProjectsTablesRestoreRequest,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsTableTemplatesUseResponse201:
        """Restore deleted table

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}/restore")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}/restore", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "POST", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/projects/{project_id}/tables/{table_id}/restore",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def update(self, project_id: str, table_id: str, body: UpdateProjectsTableRequest,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsTableTemplatesUseResponse201:
        """Update table

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/tables/{quote(table_id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "table_id": table_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/tables/{table_id}", _path_params)
        _concrete_selector = "PATCH " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "PATCH",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "PATCH", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="PATCH /v1/projects/{project_id}/tables/{table_id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "PATCH",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)


class _SyncTableTemplateResource:
    def __init__(self, _client: "SDK") -> None:
        self._client = _client

    def create(self, body: CreateTableTemplateRequest,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> GetProjectsTableTemplateResponse200:
        """Create table template

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, "/v1/table-templates")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = None
        _concrete_path = interpolate_path("/v1/table-templates", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "POST", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/table-templates",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def delete(self, template_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> DeleteOrganizationsWebhookResponse200:
        """Delete table template

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/table-templates/{quote(template_id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"template_id": template_id}
        _concrete_path = interpolate_path("/v1/table-templates/{template_id}", _path_params)
        _concrete_selector = "DELETE " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "DELETE",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "DELETE", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="DELETE /v1/table-templates/{template_id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "DELETE",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def list_mine(self,
        *,
        cursor: str | None = None,
        filter: str | None = None,
        lang: str | None = None,
        order: str | None = None,
        page: int | None = None,
        q: str | None = None,
        select: str | None = None,
        limit: int | None = None,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> ListProjectsTableTemplatesResponse200:
        """List my table templates

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, "/v1/table-templates/mine")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {"cursor": cursor, "filter": filter, "lang": lang, "order": order, "page": page, "q": q, "select": select, "limit": limit}
        _path_params: dict[str, str] | None = None
        _concrete_path = interpolate_path("/v1/table-templates/mine", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/table-templates/mine",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def project_get(self, project_id: str, template_id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> GetProjectsTableTemplateResponse200:
        """Preview table template

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/table-templates/{quote(template_id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "template_id": template_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/table-templates/{template_id}", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/table-templates/{template_id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def project_list(self, project_id: str,
        *,
        cursor: str | None = None,
        filter: str | None = None,
        lang: str | None = None,
        order: str | None = None,
        page: int | None = None,
        q: str | None = None,
        select: str | None = None,
        limit: int | None = None,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> ListProjectsTableTemplatesResponse200:
        """Browse table templates

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/table-templates")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {"cursor": cursor, "filter": filter, "lang": lang, "order": order, "page": page, "q": q, "select": select, "limit": limit}
        _path_params: dict[str, str] | None = {"project_id": project_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/table-templates", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/projects/{project_id}/table-templates",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def update(self, template_id: str, body: UpdateTableTemplateRequest,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> GetProjectsTableTemplateResponse200:
        """Update table template

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/table-templates/{quote(template_id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"template_id": template_id}
        _concrete_path = interpolate_path("/v1/table-templates/{template_id}", _path_params)
        _concrete_selector = "PATCH " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "PATCH",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "PATCH", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="PATCH /v1/table-templates/{template_id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "PATCH",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def use(self, project_id: str, template_id: str, body: CreateProjectsTableTemplatesUseRequest,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateProjectsTableTemplatesUseResponse201:
        """Create table from template

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/projects/{quote(project_id, safe='')}/table-templates/{quote(template_id, safe='')}/use")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"project_id": project_id, "template_id": template_id}
        _concrete_path = interpolate_path("/v1/projects/{project_id}/table-templates/{template_id}/use", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "POST", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/projects/{project_id}/table-templates/{template_id}/use",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)


class _SyncWebhookResource:
    def __init__(self, _client: "SDK") -> None:
        self._client = _client

    def create(self, organization_id: str, body: CreateOrganizationsWebhookRequest,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateOrganizationsWebhookResponse201:
        """Create webhook

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/organizations/{quote(organization_id, safe='')}/webhooks")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"organization_id": organization_id}
        _concrete_path = interpolate_path("/v1/organizations/{organization_id}/webhooks", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "POST", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/organizations/{organization_id}/webhooks",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def delete(self, organization_id: str, id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> DeleteOrganizationsWebhookResponse200:
        """Delete webhook

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/organizations/{quote(organization_id, safe='')}/webhooks/{quote(id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"organization_id": organization_id, "id": id}
        _concrete_path = interpolate_path("/v1/organizations/{organization_id}/webhooks/{id}", _path_params)
        _concrete_selector = "DELETE " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "DELETE",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "DELETE", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="DELETE /v1/organizations/{organization_id}/webhooks/{id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "DELETE",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def deliveries(self, organization_id: str, id: str,
        *,
        cursor: str | None = None,
        filter: str | None = None,
        lang: str | None = None,
        order: str | None = None,
        page: int | None = None,
        q: str | None = None,
        select: str | None = None,
        limit: int | None = None,
        event: Literal["batch.complete", "batch.failed", "batch.partial", "ping"] | None = None,
        status: Literal["pending", "success", "failed"] | None = None,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> ListOrganizationsWebhooksDeliveriesResponse200:
        """List webhook deliveries

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/organizations/{quote(organization_id, safe='')}/webhooks/{quote(id, safe='')}/deliveries")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {"cursor": cursor, "filter": filter, "lang": lang, "order": order, "page": page, "q": q, "select": select, "limit": limit, "event": event, "status": status}
        _path_params: dict[str, str] | None = {"organization_id": organization_id, "id": id}
        _concrete_path = interpolate_path("/v1/organizations/{organization_id}/webhooks/{id}/deliveries", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/organizations/{organization_id}/webhooks/{id}/deliveries",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def get(self, organization_id: str, id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> GetOrganizationsWebhookResponse200:
        """Get webhook

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/organizations/{quote(organization_id, safe='')}/webhooks/{quote(id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"organization_id": organization_id, "id": id}
        _concrete_path = interpolate_path("/v1/organizations/{organization_id}/webhooks/{id}", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/organizations/{organization_id}/webhooks/{id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def list(self, organization_id: str,
        *,
        cursor: str | None = None,
        filter: str | None = None,
        lang: str | None = None,
        order: str | None = None,
        page: int | None = None,
        q: str | None = None,
        select: str | None = None,
        limit: int | None = None,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> ListOrganizationsWebhooksResponse200:
        """List webhooks

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/organizations/{quote(organization_id, safe='')}/webhooks")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {"cursor": cursor, "filter": filter, "lang": lang, "order": order, "page": page, "q": q, "select": select, "limit": limit}
        _path_params: dict[str, str] | None = {"organization_id": organization_id}
        _concrete_path = interpolate_path("/v1/organizations/{organization_id}/webhooks", _path_params)
        _concrete_selector = "GET " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "GET",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "GET", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="GET /v1/organizations/{organization_id}/webhooks",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "GET",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def rotate_secret(self, organization_id: str, id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateOrganizationsWebhookResponse201:
        """Rotate webhook secret

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/organizations/{quote(organization_id, safe='')}/webhooks/{quote(id, safe='')}/rotate-secret")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"organization_id": organization_id, "id": id}
        _concrete_path = interpolate_path("/v1/organizations/{organization_id}/webhooks/{id}/rotate-secret", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "POST", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/organizations/{organization_id}/webhooks/{id}/rotate-secret",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def test(self, organization_id: str, id: str,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> CreateOrganizationsWebhooksTestResponse200:
        """Send test webhook

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/organizations/{quote(organization_id, safe='')}/webhooks/{quote(id, safe='')}/test")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"organization_id": organization_id, "id": id}
        _concrete_path = interpolate_path("/v1/organizations/{organization_id}/webhooks/{id}/test", _path_params)
        _concrete_selector = "POST " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "POST",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "POST", url,
            headers=_headers, json=None, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="POST /v1/organizations/{organization_id}/webhooks/{id}/test",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "POST",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)

    def update(self, organization_id: str, id: str, body: UpdateOrganizationsWebhookRequest,
        *,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        cancel_token: "threading.Event | None" = None
    ) -> GetOrganizationsWebhookResponse200:
        """Update webhook

        Raises:
            BadRequestError: HTTP 400
            UnauthorizedError: HTTP 401
            ForbiddenError: HTTP 403
            APIStatusError: HTTP 413
            APIStatusError: HTTP 415
            InternalServerError: HTTP 500
        """
        url = _build_url(self._client._config.base_url, f"/v1/organizations/{quote(organization_id, safe='')}/webhooks/{quote(id, safe='')}")
        _headers = _build_headers(self._client._config, extra=headers)
        _params: dict[str, Any] = {}
        _path_params: dict[str, str] | None = {"organization_id": organization_id, "id": id}
        _concrete_path = interpolate_path("/v1/organizations/{organization_id}/webhooks/{id}", _path_params)
        _concrete_selector = "PATCH " + _concrete_path
        _request_meta = self._client._stale_tracker.build_request_meta(
            _concrete_selector, _concrete_path, "PATCH",
        )
        _response = _do_request_sync(
            self._client._sync_client, self._client._config, "PATCH", url,
            headers=_headers, json=body, params=_params, timeout=timeout,
            cancel_token=cancel_token, operation="PATCH /v1/organizations/{organization_id}/webhooks/{id}",
            request_meta=_request_meta,
        )
        if _response.status_code < 400:
            self._client._stale_tracker.mark_stale(
                [], _path_params, _concrete_selector,
            )
            if _request_meta is not None and _request_meta.is_stale:
                self._client._stale_tracker.clear_stale(
                    _concrete_selector, _concrete_path, "PATCH",
                    _request_meta.seq_snapshot,
                )
        _raise_for_status(_response)
        return _parse_body(_response)


class SDK:
    def __init__(self, config: ClientConfig) -> None:
        self._config = config
        self._sync_client = httpx.Client(
            transport=config.sync_transport,
        )
        _inv = config.invalidation
        self._stale_tracker = _StaleTrackerSync(
            stale_time=_inv.stale_time if _inv is not None else 0.0,
            stale_max_entries=(
                _inv.stale_max_entries if _inv is not None else 1000
            ),
            max_sources_per_target=(
                _inv.max_sources_per_target if _inv is not None else 16
            ),
        )
        self.batch = _SyncBatchResource(self)
        self.column = _SyncColumnResource(self)
        self.export = _SyncExportResource(self)
        self.extract = _SyncExtractResource(self)
        self.row = _SyncRowResource(self)
        self.suggest = _SyncSuggestResource(self)
        self.table = _SyncTableResource(self)
        self.tableTemplate = _SyncTableTemplateResource(self)
        self.webhook = _SyncWebhookResource(self)

    def is_stale(self, method: str, path: str) -> bool:
        """Returns True when (method, path) sits inside an active stale window."""
        return self._stale_tracker.is_stale(method, path)


class AsyncSDK:
    def __init__(self, config: ClientConfig) -> None:
        self._config = config
        self._async_client = httpx.AsyncClient(
            transport=config.transport,
        )
        _inv = config.invalidation
        self._stale_tracker = _StaleTracker(
            stale_time=_inv.stale_time if _inv is not None else 0.0,
            stale_max_entries=(
                _inv.stale_max_entries if _inv is not None else 1000
            ),
            max_sources_per_target=(
                _inv.max_sources_per_target if _inv is not None else 16
            ),
        )
        self.batch = _BatchResource(self)
        self.column = _ColumnResource(self)
        self.export = _ExportResource(self)
        self.extract = _ExtractResource(self)
        self.row = _RowResource(self)
        self.suggest = _SuggestResource(self)
        self.table = _TableResource(self)
        self.tableTemplate = _TableTemplateResource(self)
        self.webhook = _WebhookResource(self)

    async def is_stale(self, method: str, path: str) -> bool:
        """Returns True when (method, path) sits inside an active stale window."""
        return await self._stale_tracker.is_stale(method, path)
