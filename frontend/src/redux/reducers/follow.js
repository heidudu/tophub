const initialState = {
  followList:[],
  followDetailList:[]
};
//此处用redux范式化处理可能会比较简洁明了
export default (state = JSON.parse(JSON.stringify(initialState)),action) => {
  switch (action.type) {
    case "GET_FOLLOW_LIST" :
      if (action.followList)  state.followList=action.followList;
      break;
    case "GET_FOLLOW_DETAIL_LIST" :
      state.followDetailList=action.followDetailList;
      break;

    case "ADD_FOLLOW":
      if (action.target)  state.followList=state.followList.concat(action.target);
      break;
    case "REMOVE_FOLLOW":
      if (action.target&& state.followList.indexOf(action.target)>-1)  state.followList.splice(state.followList.indexOf(action.target),1);
      break;

    default:
      return state
  }
  return JSON.parse(JSON.stringify(state))
}


export const getFollowList = (state) => state.follow.followList;
export const getFollowDetailList = (state) => state.follow.followDetailList;
