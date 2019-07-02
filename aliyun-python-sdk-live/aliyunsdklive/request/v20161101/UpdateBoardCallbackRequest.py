# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class UpdateBoardCallbackRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'live', '2016-11-01', 'UpdateBoardCallback','live')

	def get_AuthKey(self):
		return self.get_query_params().get('AuthKey')

	def set_AuthKey(self,AuthKey):
		self.add_query_param('AuthKey',AuthKey)

	def get_CallbackEnable(self):
		return self.get_query_params().get('CallbackEnable')

	def set_CallbackEnable(self,CallbackEnable):
		self.add_query_param('CallbackEnable',CallbackEnable)

	def get_CallbackEvents(self):
		return self.get_query_params().get('CallbackEvents')

	def set_CallbackEvents(self,CallbackEvents):
		self.add_query_param('CallbackEvents',CallbackEvents)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_CallbackUri(self):
		return self.get_query_params().get('CallbackUri')

	def set_CallbackUri(self,CallbackUri):
		self.add_query_param('CallbackUri',CallbackUri)

	def get_AppId(self):
		return self.get_query_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_query_param('AppId',AppId)

	def get_AuthSwitch(self):
		return self.get_query_params().get('AuthSwitch')

	def set_AuthSwitch(self,AuthSwitch):
		self.add_query_param('AuthSwitch',AuthSwitch)