const initialState = {
  topicNav:null,
  topicItems:[],
  next_page:1,
  has_next:true,
};

export default (state = JSON.parse(JSON.stringify(initialState)),action) => {
  switch (action.type) {
    case "SET_TOPIC_NAV" :
      if (action.topicNav)  state.topicNav=action.topicNav;
      break;
    case "SET_TOPIC_ITEMS":
      if(state.next_page===action.current_page){
        state.topicItems=state.topicItems.concat(action.topicItems);
        state.next_page = state.next_page+1;
        state.has_next=action.has_next;
      }

      break;
    case "RESET_TOPIC_ITEMS":
      state.topicItems=[];
      state.next_page=1;
      state.has_next=true;
      break;
    default:
      return state
  }
  return JSON.parse(JSON.stringify(state))
}

// 获取登录用户的信息
export const getTopicNav = (state) => state.topic.topicNav;
export const getTopicItems = (state) => state.topic.topicItems;
export const getTopicItemsHasNext = (state) => state.topic.has_next;
export const getTopicItemsNextPage= (state) => state.topic.next_page;