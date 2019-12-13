import React, {useEffect} from 'react';
import './style.scss'
import MainColumn from '../../layout/main'
import Card from '../../components/card-list'
import './style.scss'
import store from "../../redux";
import { useSelector} from 'react-redux';
import {getTopicItems,getTopicItemsHasNext,getTopicItemsNextPage} from "../../redux/reducers/topic";
import {setTopicItems,resetTopicItems} from "../../redux/actions/topic"
import InfiniteScroll from "react-infinite-scroller";
import Loading from "../../components/common/loading"






export default function (props) {

  const id = props.match.params.id;
  const topicItems = useSelector((state) => getTopicItems(state));
  const hasNext = useSelector((state) => getTopicItemsHasNext(state));
  const next_page = useSelector((state) => getTopicItemsNextPage(state));



  useEffect(()=>{
    resetTopicItems()(store.dispatch, store.getState)
  },[id]);

  const loadMore = function() {
    if(hasNext) {
      setTopicItems(id,next_page)(store.dispatch, store.getState)
    }
  };

  return(

    <MainColumn>
      <InfiniteScroll
        loadMore={loadMore}
        hasMore={hasNext}
        loader={<Loading />}
        threshold={100}
        useWindow={false}
      >
        <Card list={topicItems} />
      </InfiniteScroll>
    </MainColumn>
  )
}