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
from aliyunsdkdms_enterprise.endpoint import endpoint_data

class RevokeUserPermissionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dms-enterprise', '2018-11-01', 'RevokeUserPermission','dmsenterprise')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_PermTypes(self):
		return self.get_query_params().get('PermTypes')

	def set_PermTypes(self,PermTypes):
		self.add_query_param('PermTypes',PermTypes)

	def get_UserAccessId(self):
		return self.get_query_params().get('UserAccessId')

	def set_UserAccessId(self,UserAccessId):
		self.add_query_param('UserAccessId',UserAccessId)

	def get_DsType(self):
		return self.get_query_params().get('DsType')

	def set_DsType(self,DsType):
		self.add_query_param('DsType',DsType)

	def get_UserId(self):
		return self.get_query_params().get('UserId')

	def set_UserId(self,UserId):
		self.add_query_param('UserId',UserId)

	def get_Tid(self):
		return self.get_query_params().get('Tid')

	def set_Tid(self,Tid):
		self.add_query_param('Tid',Tid)

	def get_DbId(self):
		return self.get_query_params().get('DbId')

	def set_DbId(self,DbId):
		self.add_query_param('DbId',DbId)

	def get_TableId(self):
		return self.get_query_params().get('TableId')

	def set_TableId(self,TableId):
		self.add_query_param('TableId',TableId)

	def get_Logic(self):
		return self.get_query_params().get('Logic')

	def set_Logic(self,Logic):
		self.add_query_param('Logic',Logic)

	def get_TableName(self):
		return self.get_query_params().get('TableName')

	def set_TableName(self,TableName):
		self.add_query_param('TableName',TableName)