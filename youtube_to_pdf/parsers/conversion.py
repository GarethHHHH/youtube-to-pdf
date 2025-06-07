from flask_restx import reqparse
from youtube_to_pdf.utils import youtube
from youtube_to_pdf.utils import type as type_utils


def get_parser_adder() -> reqparse:
    parser = reqparse.RequestParser()
    parser.add_argument(
        "url",
        type=youtube.validate,
        help="Direct Youtube video URL",
    )
    return parser