const initialState = {
  pcActive:false,
  mobileActive:false
};

export default (state = JSON.parse(JSON.stringify(initialState)),action) => {
  switch (action.type) {
    case "REMOVE_ACTIVE_SIDEBAR" :
      if (action.data==="pc")  {state.pcActive=false}else{
        state.mobileActive=false
      }
      break;
    case "CHANGE_ACTIVE_SIDEBAR" :
      if (action.data==="pc")  {state.pcActive=!state.pcActive}else{
        state.mobileActive=!state.mobileActive
      }
      break;

    default:
      return state
  }
  return JSON.parse(JSON.stringify(state))
}


export const getPcActive = (state) => state.sidebar.pcActive;
export const getMobileActive = (state) => state.sidebar.mobileActive;