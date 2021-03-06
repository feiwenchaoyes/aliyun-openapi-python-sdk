# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest

class DetectFaceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'facebody', '2019-12-30', 'DetectFace','facebody')
		self.set_method('POST')

	def get_ImageType(self):
		return self.get_body_params().get('ImageType')

	def set_ImageType(self,ImageType):
		self.add_body_params('ImageType', ImageType)

	def get_ImageURL(self):
		return self.get_body_params().get('ImageURL')

	def set_ImageURL(self,ImageURL):
		self.add_body_params('ImageURL', ImageURL)

	def get_ImageContent(self):
		return self.get_body_params().get('ImageContent')

	def set_ImageContent(self,ImageContent):
		self.add_body_params('ImageContent', ImageContent)