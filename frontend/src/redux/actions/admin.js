import {
  _getAdminNodesRequest,
  _addAdminNodesRequest,
  _deleteAdminNodesRequest,
  _updateAdminNodesRequest,
  _getAdminSourceRequest,
  _addAdminSourceRequest,
  _deleteAdminSourceRequest,
  _updateAdminSourceRequest,
  _getAdminTopicRequest,
  _addAdminTopicRequest,
  _deleteAdminTopicRequest,
  _updateAdminTopicRequest,
  _getAdminSpiderRequest,
  _updateAdminSpiderRequest,
  _runAdminSpiderRequest,
  _stopAdminSpiderRequest
} from "../../api";


export const loadAdminNodes = () => {
  return (dispatch,getState) => {
    return new Promise(async (resolve,reject) =>{
      dispatch({type:'RESET_ADMIN_NODES'});
      await _getAdminNodesRequest().then(([err,res]) => {
        if (err)  return resolve([ err ? err : '未知错误',null ]);
        if (res && res.success){
          console.log(res.data);
          dispatch({type:'LOAD_ADMIN_NODES',adminNodes:res.data});

        }
        resolve([null,res])
      })

    })
  }
};

export const addAdminNodes = (newData) => {
  return (dispatch,getState) => {
    return new Promise(async (resolve,reject) =>{
      return  await _addAdminNodesRequest(newData).then(([err,res]) => {
        if (err)  return resolve([ err ? err : '未知错误',null ]);
        if (res && res.success){
          console.log(res.data);
          dispatch({type:'ADD_ADMIN_NODES',newData:newData});
        }
        resolve([null,res])
      })


    })
  }
};

export const updateAdminNodes = (newData,oldData) => {
  return (dispatch,getState) => {
    return new Promise(async (resolve,reject) =>{
      return  await _updateAdminNodesRequest(newData,oldData).then(([err,res]) => {
        if (err)  return resolve([ err ? err : '未知错误',null ]);
        if (res && res.success){
          console.log(res.data);
          dispatch({type:'UPDATE_ADMIN_NODES',oldData:oldData,newData:newData});
        }
        resolve([null,res])
      })


    })
  }
};

export const deleteAdminNodes = (oldData) => {
  return (dispatch,getState) => {
    return new Promise(async (resolve,reject) =>{
      return  await _deleteAdminNodesRequest(oldData).then(([err,res]) => {
        if (err)  return resolve([ err ? err : '未知错误',null ]);
        if (res && res.success){
          console.log(res.data);
          dispatch({type:'DELETE_ADMIN_NODES',oldData:oldData});
        }
        resolve([null,res])
      })


    })
  }
};

//source 处理
export const loadAdminSource = () => {
  return (dispatch,getState) => {
    return new Promise(async (resolve,reject) =>{
      dispatch({type:'RESET_ADMIN_SOURCE'});
      await _getAdminSourceRequest().then(([err,res]) => {
        if (err)  return resolve([ err ? err : '未知错误',null ]);
        if (res && res.success){
          console.log(res.data);
          dispatch({type:'LOAD_ADMIN_SOURCE',adminSource:res.data});
        }
        resolve([null,res])
      })

    })
  }
};

export const addAdminSource = (newData) => {
  return (dispatch,getState) => {
    return new Promise(async (resolve,reject) =>{
      return  await _addAdminSourceRequest(newData).then(([err,res]) => {
        if (err)  return resolve([ err ? err: '未知错误',null ]);
        if (res && res.success){
          console.log(res.data);
          dispatch({type:'ADD_ADMIN_SOURCE',newData:newData});
        }
        resolve([null,res])
      })


    })
  }
};

export const updateAdminSource = (newData,oldData) => {
  return (dispatch,getState) => {
    return new Promise(async (resolve,reject) =>{
      return  await _updateAdminSourceRequest(newData,oldData).then(([err,res]) => {
        if (err)  return resolve([ err ? err : '未知错误',null ]);
        if (res && res.success){
          console.log(res.data);
          dispatch({type:'UPDATE_ADMIN_SOURCE',oldData:oldData,newData:newData});
        }
        resolve([null,res])
      })


    })
  }
};

export const deleteAdminSource = (oldData) => {
  return (dispatch,getState) => {
    return new Promise(async (resolve,reject) =>{
      return  await _deleteAdminSourceRequest(oldData).then(([err,res]) => {
        if (err)  return resolve([ err ? err: '未知错误',null ]);
        if (res && res.success){
          console.log(res.data);
          dispatch({type:'DELETE_ADMIN_SOURCE',oldData:oldData});
        }
        resolve([null,res])
      })


    })
  }
};

//topic处理

export const loadAdminTopic = () => {
  return (dispatch,getState) => {
    return new Promise(async (resolve,reject) =>{
      dispatch({type:'RESET_ADMIN_TOPIC'});
      await _getAdminTopicRequest().then(([err,res]) => {
        if (err)  return resolve([ err ? err: '未知错误',null ]);
        if (res && res.success){
          console.log(res.data);
          dispatch({type:'LOAD_ADMIN_TOPIC',adminTopic:res.data});
        }
        resolve([null,res])
      })

    })
  }
};

export const addAdminTopic = (newData) => {
  return (dispatch,getState) => {
    return new Promise(async (resolve,reject) =>{
      return  await _addAdminTopicRequest(newData).then(([err,res]) => {
        if (err)  return resolve([ err ? err: '未知错误',null ]);
        if (res && res.success){
          console.log(res.data);
          dispatch({type:'ADD_ADMIN_TOPIC',newData:newData});
        }
        resolve([null,res])
      })


    })
  }
};

export const updateAdminTopic = (newData,oldData) => {
  return (dispatch,getState) => {
    return new Promise(async (resolve,reject) =>{
      return  await _updateAdminTopicRequest(newData,oldData).then(([err,res]) => {
        if (err)  return resolve([ err ? err : '未知错误',null ]);
        if (res && res.success){
          console.log(res.data);
          dispatch({type:'UPDATE_ADMIN_TOPIC',oldData:oldData,newData:newData});
        }
        res([null,res])
      })


    })
  }
};

export const deleteAdminTopic = (oldData) => {
  return (dispatch,getState) => {
    return new Promise(async (resolve,reject) =>{
      return  await _deleteAdminTopicRequest(oldData).then(([err,res]) => {
        if (err)  return resolve([ err ? err: '未知错误',null ]);
        if (res && res.success){
          console.log(res.data);
          dispatch({type:'DELETE_ADMIN_TOPIC',oldData:oldData});
        }
        resolve([null,res])
      })


    })
  }
};

//spider 处理
export const loadAdminSpider = () => {
  return (dispatch,getState) => {
    return new Promise(async (resolve,reject) =>{
      dispatch({type:'RESET_ADMIN_SPIDER'});
      await _getAdminSpiderRequest().then(([err,res]) => {
        if (err)  return resolve([ err ? err: '未知错误',null ]);
        if (res && res.success){
          console.log(res.data);
          dispatch({type:'LOAD_ADMIN_SPIDER',adminSpider:res.data});
        }
        resolve([null,res])

      })
    })
  }
};

export const updateAdminSpider = (newData,oldData) => {
  return (dispatch,getState) => {
    return new Promise(async (resolve,reject) =>{
      return  await _updateAdminSpiderRequest(newData,oldData).then(([err,res]) => {
        if (err)  return resolve([ err ? err: '未知错误',null ]);
        if (res && res.success) {
          console.log(res.data);
          dispatch({type: 'UPDATE_ADMIN_SPIDER', oldData: oldData, newData: newData});
        }
        resolve([null,res])
      })


    })
  }
};

export const runAdminSpider = (data) => {
  return (dispatch,getState) => {
    return new Promise(async (resolve,reject) =>{
      return  await _runAdminSpiderRequest(data).then(([err,res]) => {
        if (err)  return resolve([ err ? err : '未知错误',null ]);
        if (res && res.success){
          console.log(res.data);
          dispatch({type:'RUN_ADMIN_SPIDER',data:data});
        }
        resolve([null,res])
      })

    })
  }
};

export const stopAdminSpider = (data) => {
  return (dispatch,getState) => {
    return new Promise(async (resolve,reject) =>{
      return  await _stopAdminSpiderRequest(data).then(([err,res]) => {
        if (err)  return resolve([ err ? err : '未知错误',null ]);
        if (res && res.success){
          console.log(res.data);
          dispatch({type:'STOP_ADMIN_SPIDER',data:data});
        }
        resolve([null,res])
      })

    })
  }
};