from django.apps import AppConfig


# class FindStateConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'find_state'


class FindStateConfig(AppConfig):
    name = 'find_state'

    def ready(self):
        from CityStateMap.urls import api_router
        from find_state.views import router

        api_router.include_router(router, tags=[self.name])