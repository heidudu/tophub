import {_getUserInfoRequest} from "../../api";

export const loadUserInfo = () => {
  return (dispatch,getState) => {
    return new Promise(async (resolve,reject) =>{
      await _getUserInfoRequest().then(([err,res]) => {
        if (err)  return resolve([ err ? err.message : '未知错误' ,null]);
        if (res && res.success){
          console.log(res.data);
          dispatch({type:'SET_USER',userinfo:res.data});
        }
        resolve([null,res])
      })

    })
  }
};




