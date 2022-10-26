"""Stream type classes for tap-gainsightpx."""
from typing import Any, Dict, Optional

from singer_sdk import typing as th

from tap_gainsightpx.client import GainsightPXStream


class EngagementsStream(GainsightPXStream):
    """Engagements Stream."""

    name = "engagements"
    path = "/engagement"
    records_jsonpath = "$.engagements[*]"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("description", th.StringType),
        th.Property("envs", th.ArrayType(th.StringType)),
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("propertyKeys", th.ArrayType(th.StringType)),
        th.Property("state", th.StringType),
        th.Property("type", th.StringType),
    ).to_dict()

    def add_more_url_params(
        self, params: dict, next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Add more params specific to the stream."""
        params["filter"] = ";".join(
            [
                f"date>={self.config['start_date']}",
                f"date<={self.config['end_date']}",
            ]
        )
        if next_page_token:
            params["pageNumber"] = next_page_token
        return params


class SurveyResponsesStream(GainsightPXStream):
    """Survey Responses Stream."""

    name = "survey_responses"
    path = "/survey/responses"
    records_jsonpath = "$.results[*]"
    primary_keys = ["eventId"]
    replication_key = "date"
    schema = th.PropertiesList(
        th.Property("eventId", th.StringType),
        th.Property("identifyId", th.StringType),
        th.Property("propertyKey", th.StringType),
        th.Property("date", th.IntegerType),
        th.Property("eventType", th.StringType),
        th.Property("sessionId", th.StringType),
        th.Property("userType", th.StringType),
        th.Property("accountId", th.StringType),
        th.Property("globalContext", th.ObjectType()),
        th.Property("engagementId", th.StringType),
        th.Property("engagementTrackType", th.StringType),
        th.Property("contentId", th.StringType),
        th.Property("contentType", th.StringType),
        th.Property(
            "executionDate",
            th.IntegerType,
            description="Will be the same on all events related to a single "
            "engagement view, e.g. separate answers for "
            "multi-question surveys",
        ),
        th.Property(
            "executionId",
            th.StringType,
            description="Will be the same on all events related to a single "
            "engagement view, e.g. separate answers for "
            "multi-question surveys",
        ),
        th.Property("viewEventId", th.StringType),
        th.Property("carouselState", th.StringType),
        th.Property("slideId", th.StringType),
        th.Property("sequenceNumber", th.IntegerType),
        th.Property("linkUrl", th.StringType),
        th.Property("guideState", th.StringType),
        th.Property("stepId", th.StringType),
        th.Property("surveyState", th.StringType),
        th.Property("contactMeAllowed", th.BooleanType),
        th.Property("score", th.IntegerType),
        th.Property("comment", th.StringType),
        th.Property("questionType", th.StringType),
        th.Property("selectionIds", th.ArrayType(th.StringType)),
        th.Property("path", th.StringType),
    ).to_dict()

    def add_more_url_params(
        self, params: dict, next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Add more params specific to the stream."""
        if next_page_token:
            params["scrollId"] = next_page_token
        return params


class AccountsStream(GainsightPXStream):
    """Accounts Stream."""

    name = "accounts"
    path = "/accounts"
    records_jsonpath = "$.accounts[*]"
    primary_keys = ["id"]
    replication_key = "lastModifiedDate"
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("trackedSubscriptionId", th.StringType),
        th.Property("sfdcId", th.StringType),
        th.Property("lastSeenDate", th.IntegerType),
        th.Property("dunsNumber", th.StringType),
        th.Property("industry", th.StringType),
        th.Property("numberOfEmployees", th.IntegerType),
        th.Property("sicCode", th.StringType),
        th.Property("website", th.StringType),
        th.Property("naicsCode", th.StringType),
        th.Property("plan", th.StringType),
        th.Property("location", th.ObjectType()),
        th.Property("numberOfUsers", th.IntegerType),
        th.Property("propertyKeys", th.ArrayType(th.StringType)),
        th.Property("createDate", th.IntegerType),
        th.Property("lastModifiedDate", th.IntegerType),
        th.Property("customAttributes", th.ObjectType()),
        th.Property("parentGroupId", th.StringType),
    ).to_dict()

    def add_more_url_params(
        self, params: dict, next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Add more params specific to the stream."""
        if next_page_token:
            params["scrollId"] = next_page_token

            # todo: enable replication key method
            # bookmarks = self.stream_state['bookmarks']
            # replication_key_value = bookmarks[self.name]['replication_key_value']
            # params["filter"] = ";".join([
            #     f"{self.replication_key}>{replication_key_value}",
            # ])
        return params


class FeaturesStream(GainsightPXStream):
    """Features Stream."""

    name = "features"
    path = "/feature"
    records_jsonpath = "$.features[*]"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("type", th.StringType),
        th.Property("parentFeatureId", th.StringType),
        th.Property("propertyKey", th.StringType),
        th.Property("status", th.StringType),
    ).to_dict()

    def add_more_url_params(
        self, params: dict, next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Add more params specific to the stream."""
        if params["pageSize"] > 200:
            params["pageSize"] = 200
        if next_page_token:
            params["pageNumber"] = next_page_token
        return params


class PageViewEventsStream(GainsightPXStream):
    """Page View Events Stream."""

    name = "page_view_events"
    path = "/events/pageView"
    records_jsonpath = "$.results[*]"
    primary_keys = ["eventId"]
    replication_key = "date"
    schema = th.PropertiesList(
        th.Property("eventId", th.StringType),
        th.Property("identifyId", th.StringType),
        th.Property("propertyKey", th.StringType),
        th.Property("date", th.IntegerType),
        th.Property("eventType", th.StringType),
        th.Property("sessionId", th.StringType),
        th.Property("userType", th.StringType),
        th.Property("accountId", th.StringType),
        th.Property("globalContext", th.ObjectType()),
        th.Property("scheme", th.StringType),
        th.Property("host", th.StringType),
        th.Property("path", th.StringType),
        th.Property("queryString", th.StringType),
        th.Property("hash", th.StringType),
        th.Property("queryParams", th.ObjectType()),
        th.Property("remoteHost", th.StringType),
        th.Property("referrer", th.StringType),
        th.Property("screenHeight", th.IntegerType),
        th.Property("screenWidth", th.IntegerType),
        th.Property("languages", th.ArrayType(th.StringType)),
        th.Property("pageTitle", th.StringType),
    ).to_dict()

    def add_more_url_params(
        self, params: dict, next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Add more params specific to the stream."""
        params["filter"] = ";".join(
            [
                f"date>={self.config['start_date']}",
                f"date<={self.config['end_date']}",
            ]
        )
        if next_page_token:
            params["scrollId"] = next_page_token
        return params
