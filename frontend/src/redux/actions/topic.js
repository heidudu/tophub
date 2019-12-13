import {_getTopicNavRequest, _getTopicItemsRequest} from "../../api";


export const loadTopicNav = () =>{
  return (dispatch,getState) => {
    return new Promise(async (resolve,reject) =>{
      await _getTopicNavRequest().then(([err,res]) => {
        if (err)  return resolve([ err ? err.message : '未知错误' ]);
        if (res && res.success){
          console.log(res.data);
          dispatch({type:'SET_TOPIC_NAV',topicNav:res.data});
        }
        resolve([null,res])
      })
    })
  }
};


export const setTopicItems = (id,page) =>{
  return (dispatch,getState) => {
    return new Promise(async (resolve,reject) => {
      await _getTopicItemsRequest(id,page).then(([err,res]) =>{
        if (err)  return resolve([ err ? err.message : '未知错误' ,null]);
        if (res && res.success){
          console.log(res.data);
          dispatch({type:'SET_TOPIC_ITEMS',topicItems:res.data,has_next: res.has_next,current_page: res.current_page});
        }
        resolve([null,res])

      })
    })
  }
}

export const resetTopicItems = () =>{
  return (dispatch,getState) => {
    return new Promise(async (resolve,reject) => {
      dispatch({type:'RESET_TOPIC_ITEMS'});
      resolve()
    })
  }
}