from flask_restful import Resource, reqparse

from whatabot.search import wikipedia
from whatabot.ia.text import summarize


class SubjectAndSummaryResource(Resource):

    attr = reqparse.RequestParser()
    attr.add_argument(
        'subject', type=str, required=True, help='Subject to Summarize')
    
    def post(self):
        data = self.attr.parse_args()
        
        try: 
            document = wikipedia.query_by_subject(data.get('subject', ''))
            summary = summarize(document)
        except Exception as e:
            print('[ERROR]', e)
            return { 
                'msg': 'Failed', 
                'Causing': 'Error handling with the summarization' 
            }, 500

        return { 'msg': 'Success', 'summary': summary }, 200