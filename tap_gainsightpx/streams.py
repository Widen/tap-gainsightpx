"""Stream type classes for tap-gainsightpx."""

from singer_sdk import typing as th

from tap_gainsightpx.client import GainsightPXStream


class EngagementStream(GainsightPXStream):
    """Define custom stream."""

    name = "engagement"
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


class SurveyResponse(GainsightPXStream):
    """Define custom stream."""

    name = "survey_response"
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
