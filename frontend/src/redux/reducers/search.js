const initialState = {
  searchList:null,
};

export default (state = JSON.parse(JSON.stringify(initialState)),action) => {
  switch (action.type) {
    case "SET_SEARCH_LIST" :
      if (action.searchList)  state.searchList=action.searchList;
      break;
    case "RESET_SEARCH_LIST" :
      state.searchList=null;
      break;

    default:
      return state
  }
  return JSON.parse(JSON.stringify(state))
}

// 获取登录用户的信息
export const getSearchList = (state) => state.search.searchList;