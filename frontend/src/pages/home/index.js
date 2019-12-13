import React, {useEffect, useState} from 'react';
import './style.scss'
import MainColumn from '../../layout/main'
import Card from '../../components/card-list'
import store from "../../redux";
import { useSelector} from 'react-redux';
import {getFollowDetailList,getFollowList} from "../../redux/reducers/follow";
import {setFollowDetailList} from "../../redux/actions/follow"
import Toastify from "toastify-js";
import Loading from "../../components/common/loading";
import {getUserInfo} from "../../redux/reducers/user";





export default function (props) {


  const followDetailList = useSelector((state) => getFollowDetailList(state));
  const followList = useSelector((state) => getFollowList(state));
  const [loading,setLoading] = useState(true);
  const me = useSelector((state) => getUserInfo(state));

  useEffect(()=>{
    if(me) {
      setFollowDetailList()(store.dispatch, store.getState).then(function ([err, res]) {
        if (err) {
          Toastify({
            text: err,
            duration: 3000,
            backgroundColor: 'linear-gradient(to right, #0988fe, #1c75fb)'
          }).showToast()
        } else {
          setLoading(false)
        }
      })
    }else{
      setLoading(false)
    }
  },[followList.length,me]);

  if(loading){return <MainColumn><Loading /></MainColumn> }
  else return(

    <MainColumn>
      {me?
        <>
        {followDetailList && <Card list={followDetailList}  />}
        </>
        :
        <h5 className="text-center text-muted">登录后可显示订阅内容</h5>
      }

    </MainColumn>
  )
}