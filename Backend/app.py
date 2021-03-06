#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging.config

import falcon

import messages
import middlewares
from falcon_multipart.middleware import MultipartMiddleware
from resources import common_resources, trivial_events
from settings import configure_logging

# LOGGING
mylogger = logging.getLogger(__name__)
configure_logging()


# DEFAULT 404
# noinspection PyUnusedLocal
def handle_404(req, resp):
    resp.media = messages.resource_not_found
    resp.status = falcon.HTTP_404


# FALCON
app = application = falcon.API(
    middleware=[
        middlewares.DBSessionManager(),
        middlewares.Falconi18n(),
        MultipartMiddleware()
    ]
)
application.add_route("/", common_resources.ResourceHome())

#application.add_route("/account/profile", account_resources.ResourceAccountUserProfile())
#application.add_route("/account/profile/update_profile_image", account_resources.ResourceAccountUpdateProfileImage())
#application.add_route("/account/create_token", account_resources.ResourceCreateUserToken())
#application.add_route("/account/delete_token", account_resources.ResourceDeleteUserToken())

#application.add_route("/users/register", user_resources.ResourceRegisterUser())
#application.add_route("/users/show/{username}", user_resources.ResourceGetUserProfile())
#application.add_route("/users/list", user_resources.ResourceGetUsers())

application.add_route("/trivial/question/list", trivial_events.ResourceGetQuestions())
application.add_route("/trivial/question", trivial_events.ResourceGetRandomQuestion())
application.add_route("/trivial/question/add", trivial_events.ResourceAddQuestion())

application.add_sink(handle_404, "")
