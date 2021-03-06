# Copyright (c) 2018 Fortinet, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

#    FortiAuthenticator API request format templates.

# About api request message naming regulations:
# Prefix         HTTP method
# ADD_XXX      -->    POST
# SET_XXX      -->    PUT
# DELETE_XXX   -->    DELETE
# GET_XXX      -->    GET
# MODIFY_XXX   -->    PATCH

# Activation
# query
GET_ACTIVATION = """
{
    {% if id is defined %}
        "path": "/api/v1/activation/{{ id }}/",
    {% else %}
        {% set _options = {
            "sn": sn,
            "vdom": vdom,
            "namespace_id": namespace_id,
            "customer_id": customer_id
        } %}
        {% set _query = [] %}
        {% for k, v in _options.iteritems() if v is defined %}
            {% if _query.append('&'+k+'='+v) %}
            {% endif %}
        {% endfor %}
        {% if _query %}
            {% set _query = ''.join(_query) %}
            "path": "/api/v1/activation/?{{ _query }}",
        {% else %}
            "path": "/api/v1/activation/",
        {% endif %}
    {% endif %}
    "method": "GET"
}
"""

# query
ADD_ACTIVATION = """
{
    "path": "/api/v1/activation/",
    "method": "POST",
    "body": {
        "sn": "{{ sn }}",
        "vdom": "{{ vdom }}",     
        "namespace": "{{ namespace }}"
    }
}
"""


# delete an usergroup
DELETE_ACTIVATION = """
{
    "path": "/api/v1/activation/{{ id }}/",
    "method": "DELETE"
}
"""


# vdomuser
ADD_VDOMUSER = """
{
    "path": "/api/v1/vdomuser/",
    "method": "POST",
    "body": {
        "sn": "{{ sn }}",
        "vdom": "{{ vdom }}",     
        "namespace": "{{ namespace }}",
        "email": "{{ email }}",     
        "username": "{{ username }}"
    }
}
"""

DELETE_VDOMUSER = """
{
    "path": "/api/v1/vdomuser/{{ id }}/",
    "method": "DELETE"
}
"""
