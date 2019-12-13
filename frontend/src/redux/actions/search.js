import {_getSearchListRequest} from "../../api";

export const setSearchList = (q) => {
  return (dispatch,getState) => {
    return new Promise(async (resolve,reject) =>{
      dispatch({type:'RESET_SEARCH_LIST'});
      await _getSearchListRequest(q).then(([err,res]) => {
        if (err)  return resolve([ err ? err.message : '未知错误' ,null]);
        if (res && res.success){
          console.log(res.data);
          dispatch({type:'SET_SEARCH_LIST',searchList:res.data});
        }
        resolve([null,res])
      })

    })
  }
};