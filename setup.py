# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="DCSA OpenAPI specification for Track &amp; Trace",
    author_email="info@dcsa.org",
    url="",
    keywords=["Swagger", "DCSA OpenAPI specification for Track &amp; Trace"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    Managing and sending Shipment-, Transport- and Equipment-events and subscriptions for Track &amp;amp; Trace (T&amp;amp;T). API specification issued by DCSA.org.  For explanation to specific values or objects please refer to the &lt;a href&#x3D;&#x27;https://dcsa.org/wp-content/uploads/2021/07/202108_DCSA_P1_Information-Model-v3.2_Final.pdf&#x27;&gt;Information Model v3.2&lt;/a&gt;  Polling can be done on the &lt;b&gt;GET /v2/events&lt;/b&gt; endPoint. It is also possible to setup a subscription on the &lt;b&gt;/v2/event-subscriptions&lt;/b&gt; endPoints in order to use the push model. Here events are pushed as they occur.  For a changelog please click &lt;a href&#x3D;\&quot;https://github.com/dcsaorg/DCSA-OpenAPI/blob/master/tnt/v2/README.md#v220\&quot;&gt;here&lt;/a&gt; 
    """
)
