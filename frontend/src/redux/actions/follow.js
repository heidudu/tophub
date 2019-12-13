import {_getFollowListRequest,_addFollowRequest,_addUnfollowRequest,_getFollowDetailListRequest } from "../../api";

export const loadFollowList = () =>{
  return (dispatch,getState) => {
    return new Promise(async (resolve,reject) =>{
      await _getFollowListRequest().then(([err,res]) => {
        if (err)  return resolve([ err ? err.message : '未知错误',null ]);
        if (res && res.success){
          console.log(res.data);
          dispatch({type:'GET_FOLLOW_LIST',followList:res.data});
        resolve([null,res])
        }
      })
    })
  }
};

export const follow = (id) =>{
  return (dispatch,getState) => {
    return new Promise(async (resolve,reject) =>{
      await _addFollowRequest(id).then(([err,res]) => {
        if (err)  return resolve([ err ? err : '未知错误' ,null]);
        if (res && res.success){
          console.log(res.data);
          dispatch({type:'ADD_FOLLOW',target:res.data});
        }
        resolve([null,res])
      })
    })
  }
};

export const unfollow = (id) =>{
  return (dispatch,getState) => {
    return new Promise(async (resolve,reject) =>{
      await _addUnfollowRequest(id).then(([err,res]) => {
        if (err)  return resolve([ err ? err : '未知错误',null ]);
        if (res && res.success){
          console.log(res.data);
          dispatch({type:'REMOVE_FOLLOW',target:res.data});
        }
        resolve([null,res])
      })
    })
  }
};

export const setFollowDetailList = () =>{
  return (dispatch,getState) => {
    return new Promise(async (resolve,reject) =>{
      await _getFollowDetailListRequest().then(([err,res]) => {
        if (err)  return resolve([ err ? err : '未知错误' ,null]);
        if (res && res.success){
          console.log(res.data);
          dispatch({type:'GET_FOLLOW_DETAIL_LIST',followDetailList:res.data});
        }
        resolve([null,res])
      })
    })
  }
};
