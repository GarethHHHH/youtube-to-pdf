from flask_restx import reqparse
from youtube_to_pdf.utils import youtube


def get_parser_adder() -> reqparse:
    parser = reqparse.RequestParser()
    parser.add_argument(
        "url",
        type=youtube.validate,
        help="Direct Youtube video URL",
    )
    return parser
