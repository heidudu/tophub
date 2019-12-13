

export const removeActiveSidebar = () => {
  return (dispatch,getState) => {
    if(window.innerWidth>991){
      dispatch({type:'REMOVE_ACTIVE_SIDEBAR',data:"mobile"})
    }else{
      dispatch({type:'REMOVE_ACTIVE_SIDEBAR',data:"pc"})
    }

  }
};

export const changeActiveSidebar = () => {
  return (dispatch,getState) => {
    if(window.innerWidth>991){
      dispatch({type:'CHANGE_ACTIVE_SIDEBAR',data:"pc"})
    }else{
      dispatch({type:'CHANGE_ACTIVE_SIDEBAR',data:"mobile"})
    }

  }
};