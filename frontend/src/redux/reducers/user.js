const initialState = {
  userInfo:null,
};

export default (state = JSON.parse(JSON.stringify(initialState)),action) => {
  switch (action.type) {
    case "SET_USER" :
      if (action.userinfo)  state.userInfo=action.userinfo;
      break;

    default:
      return state
  }
  return JSON.parse(JSON.stringify(state))
}

// 获取登录用户的信息
export const getUserInfo = (state) => state.user.userInfo;