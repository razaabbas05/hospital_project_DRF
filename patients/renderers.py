from rest_framework.renderers import JSONRenderer

class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context.get('response')

        if response is not None and response.status_code >= 400:
            return super().render({
                "success": False,
                "data": None,
                "message": data
            }, accepted_media_type, renderer_context)

        return super().render({
            "success": True,
            "data": data,
            "message": ""
        }, accepted_media_type, renderer_context)