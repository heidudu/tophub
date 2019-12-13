const initialState = {
  adminNodes:null,
  adminSource:null,
  adminTopic:null,
  adminSpider:null
};

export default (state = JSON.parse(JSON.stringify(initialState)),action) => {
  switch (action.type) {
    case "RESET_ADMIN_NODES" :
      state.adminNodes=null;
      break;
    case "LOAD_ADMIN_NODES" :
      state.adminNodes=action.adminNodes;
      break;
    case "ADD_ADMIN_NODES" :
      if(action.newData) state.adminNodes.data.push(action.newData);
      break;
    case "DELETE_ADMIN_NODES" :
      if(action.oldData) {
        state.adminNodes.data.splice(state.adminNodes.data.indexOf(action.oldData),1);
      }
      break;
    case "UPDATE_ADMIN_NODES" :
      state.adminNodes.data[state.adminNodes.data.indexOf(action.oldData)] = action.newData;
      break;


    case "RESET_ADMIN_SOURCE" :
      state.adminSource=null;
      break;
    case "LOAD_ADMIN_SOURCE" :
      state.adminSource=action.adminSource;
      break;
    case "ADD_ADMIN_SOURCE" :
      if(action.newData) state.adminSource.data.push(action.newData);
      break;
    case "DELETE_ADMIN_SOURCE" :
      if(action.oldData) {
        state.adminSource.data.splice(state.adminSource.data.indexOf(action.oldData),1)
      }
      break;
    case "UPDATE_ADMIN_SOURCE" :
      state.adminSource.data[state.adminSource.data.indexOf(action.oldData)] = action.newData;
      break;

    case "RESET_ADMIN_TOPIC" :
      state.adminTopic=null;
      break;
    case "LOAD_ADMIN_TOPIC" :
      state.adminTopic=action.adminTopic;
      break;
    case "ADD_ADMIN_TOPIC" :
      if(action.newData) state.adminTopic.data.push(action.newData);
      break;
    case "DELETE_ADMIN_TOPIC" :
      if(action.oldData) {
        state.adminTopic.data.splice(state.adminTopic.data.indexOf(action.oldData),1)
      }
      break;
    case "UPDATE_ADMIN_TOPIC" :
      state.adminTopic.data[state.adminTopic.data.indexOf(action.oldData)] = action.newData;
      break;

    case "RESET_ADMIN_SPIDER" :
      state.adminSpider=null;
      break;

    case "LOAD_ADMIN_SPIDER" :
      state.adminSpider=action.adminSpider;
      break;

    case "UPDATE_ADMIN_SPIDER" :
      state.adminSpider.data[state.adminSpider.data.indexOf(action.oldData)] = action.newData;
      break;

    case "RUN_ADMIN_SPIDER" :
      action.data.map(item =>{
        return (state.adminSpider.data[state.adminSpider.data.indexOf(item)].status = 1)
      });
      break;

    case "STOP_ADMIN_SPIDER" :
      action.data.map(item =>{
        return (state.adminSpider.data[state.adminSpider.data.indexOf(item)].status = 0)
      });
      break;




    default:
      return state
  }
  return JSON.parse(JSON.stringify(state))
}


export const getAdminNodes = (state) => state.admin.adminNodes;
export const getAdminSource = (state) => state.admin.adminSource;
export const getAdminTopic = (state) => state.admin.adminTopic;
export const getAdminSpider = (state) => state.admin.adminSpider;