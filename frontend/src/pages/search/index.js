import React, {useEffect, useState} from 'react';
import './style.scss'
import CenterColumn from '../../layout/center-column'
import parseUrl from "../../utils/parse-url";
import {useSelector} from "react-redux";
import {getSearchList} from "../../redux/reducers/search";
import {setSearchList} from "../../redux/actions/search";
import store from "../../redux";
import Search from '../../components/search';
import Loading from "../../components/common/loading"
import Toastify from "toastify-js";







export default function (props) {


  const q = parseUrl(props.location.search)['q'];
  const searchList = useSelector((state) => getSearchList(state));
  const [loading,setLoading] = useState(true);

  useEffect(()=>{
    setLoading(true);
    setSearchList(q)(store.dispatch, store.getState).then(function([err,res]){
      if(err){
        Toastify({
          text: err,
          duration: 3000,
          backgroundColor: 'linear-gradient(to right, #0988fe, #1c75fb)'
        }).showToast()
      }else{
        setLoading(false)
      }
    })
  },[q]);

  if(loading){return <CenterColumn><Loading /></CenterColumn> }

  return(

    <CenterColumn>
      {searchList && <Search data={searchList} />}
    </CenterColumn>
  )
}