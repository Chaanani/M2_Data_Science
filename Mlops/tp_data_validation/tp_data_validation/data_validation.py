# external imports
# import numpy as np
import pandera as pa
from marshmallow import Schema , fields
import pandas as pd

CONTENT_TYPE_LIST = [
    "video", "course", "exercise", "press_article", "web_url", "exam"
]

KEYWORDS_LIST = [
    "maths", "computer_science", "data_science",
    "history", "biology", "physics",
    "arts", "sport", "video_games",
    "economics", "social_sciences", "management"
]

YEAR_LEVEL_LIST = ["L1", "L2", "L3", "M1", "M2"]


class ParametersSchema(Schema):
    student_id = fields.Int(required=True)
    keyword = fields.Str(validate=lambda x: x in KEYWORDS_LIST, load_default=None, required=False)


parameter_schema = ParametersSchema()

CourseContentData = pa.DataFrameSchema({
    "id": pa.Column(pa.Int, checks=pa.Check.ge(0)),
    "title": pa.Column(pa.String),
    "type": pa.Column(pa.String, checks=pa.Check.isin(CONTENT_TYPE_LIST), nullable=True),
    "keyword": pa.Column(pa.String, checks=pa.Check.isin(KEYWORDS_LIST)),
    "duration": pa.Column(pa.Int, checks=pa.Check.in_range(0, 180), nullable=True),
    "creation_date": pa.Column(pa.DateTime, checks=pa.Check.ge(pd.Timestamp('1990-01-01')), nullable=True)
})

StudentProfileData = pa.DataFrameSchema({
    "student_id": pa.Column(pa.Int, checks=pa.Check.ge(0), unique=True),
    "year_level": pa.Column(pa.String, checks=pa.Check.isin(YEAR_LEVEL_LIST), nullable=True),
    "area_of_interest": pa.Column(pa.String, checks=pa.Check.isin(KEYWORDS_LIST))
})



