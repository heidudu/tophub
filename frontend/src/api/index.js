import request from'./ajax'

export const _signInRequest =  (access_token)=> {
  return request('/oauth/sign/in', 'post', {access_token},true)
};

export const _getUserInfoRequest = () => {
  return request('/api/v1/user/userinfo','get',{},true)
};

export const _signOutRequest =  ()=> {
  return request('/oauth/sign/out', 'post', {},true)
};

export const _getTopicNavRequest =  ()=> {
  return request('/api/v1/topic/nav', 'get', {},false)
};

export const _getTopicItemsRequest =  (id,page=1)=> {
  return request('/api/v1/topic/items', 'get', {"id":id,"page":page},false)
};


export const _getNodeDetailRequest =  (id)=> {
  return request('/api/v1/node/detail', 'get', {"id":id},false)
};
export const _getFollowListRequest =  ()=> {
  return request('/api/v1/follow/list', 'get', {},true)
};

export const _addFollowRequest =  (id)=> {
  return request('/api/v1/follow/add', 'post', {id},true)
};
export const _addUnfollowRequest =  (id)=> {
  return request('/api/v1/follow/remove', 'post', {id},true)
};


export const _getFollowDetailListRequest =  ()=> {
  return request('/api/v1/follow/detail', 'get', {},true)
};

export const _getSearchListRequest =  (q)=> {
  return request('/api/v1/search/list', 'get', {"q":q},false)
};

export const _getAdminNodesRequest =  ()=> {
  return request('/api/v1/admin/nodes', 'get', {},true)
};
export const _addAdminNodesRequest =  (newData)=> {
  return request('/api/v1/admin/nodes', 'post', {newData},true)
};

export const _deleteAdminNodesRequest =  (oldData)=> {
  return request('/api/v1/admin/nodes', 'delete', {oldData},true)
};

export const _updateAdminNodesRequest =  (newData,oldData)=> {
  return request('/api/v1/admin/nodes', 'put', {newData,oldData},true)
};

export const _getAdminSourceRequest =  ()=> {
  return request('/api/v1/admin/source', 'get', {},true)
};
export const _addAdminSourceRequest =  (newData)=> {
  return request('/api/v1/admin/source', 'post', {newData},true)
};

export const _deleteAdminSourceRequest =  (oldData)=> {
  return request('/api/v1/admin/source', 'delete', {oldData},true)
};

export const _updateAdminSourceRequest =  (newData,oldData)=> {
  return request('/api/v1/admin/source', 'put', {newData,oldData},true)
};


export const _getAdminTopicRequest =  ()=> {
  return request('/api/v1/admin/topic', 'get', {},true)
};
export const _addAdminTopicRequest =  (newData)=> {
  return request('/api/v1/admin/topic', 'post', {newData},true)
};

export const _deleteAdminTopicRequest =  (oldData)=> {
  return request('/api/v1/admin/topic', 'delete', {oldData},true)
};

export const _updateAdminTopicRequest =  (newData,oldData)=> {
  return request('/api/v1/admin/topic', 'put', {newData,oldData},true)
};


export const _getAdminSpiderRequest =  ()=> {
  return request('/api/v1/admin/spider', 'get', {},true)
};

export const _updateAdminSpiderRequest =  (newData,oldData)=> {
  return request('/api/v1/admin/spider', 'put', {newData,oldData},true)
};

export const _runAdminSpiderRequest =  (data)=> {
  return request('/api/v1/admin/runspider', 'post', {data},true)
};

export const _stopAdminSpiderRequest =  (data)=> {
  return request('/api/v1/admin/stopspider', 'post', {data},true)
};