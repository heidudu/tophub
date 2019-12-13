const initialState = {
  nodeDetail:null,
};

export default (state = JSON.parse(JSON.stringify(initialState)),action) => {
  switch (action.type) {
    case "SET_NODE_DETAIL" :
      if (action.nodeDetail)  state.nodeDetail=action.nodeDetail;
      break;
    case "RESET_NODE_DETAIL" :
      state.nodeDetail=null;
      break;

    default:
      return state
  }
  return JSON.parse(JSON.stringify(state))
}

// 获取登录用户的信息
export const getNodeDetail = (state) => state.node.nodeDetail;