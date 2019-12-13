import {_getNodeDetailRequest} from "../../api";

export const setNodeDetail = (id) => {
  return (dispatch,getState) => {
    return new Promise(async (resolve,reject) =>{
      dispatch({type:'RESET_NODE_DETAIL'});
      await _getNodeDetailRequest(id).then(([ err, res ]) => {
        if (err)  return resolve([ err ? err.message : '未知错误' ,null]);
        if (res && res.success){
          console.log(res.data);
          dispatch({type:'SET_NODE_DETAIL',nodeDetail:res.data});
        resolve([null,res])
        }
      })

    })
  }
};
