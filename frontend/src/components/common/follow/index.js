import React from 'react';
import './style.scss';
// import {Paperclip} from "react-feather";
import { useSelector } from 'react-redux';
import store from "../../../redux";
import { getUserInfo } from "../../../redux/reducers/user";
import { getFollowList } from "../../../redux/reducers/follow";
import {follow,unfollow } from "../../../redux/actions/follow";
import { ReactComponent as Star } from './svgs/star.svg';
import { ReactComponent as StarFilled } from './svgs/star_filled.svg';
import Toastify from 'toastify-js'

export default function(props){
  const{targetId=null, needText=false,btnLight=false} = props;

  const me = useSelector((state) => getUserInfo(state));
  const followList = useSelector((state) => getFollowList(state));

  const stopPropagation = function(e) {
    e.stopPropagation();
  };

  const handleFollow = function(e) {
    e.stopPropagation();
    follow(targetId)(store.dispatch, store.getState).then(([err,res])=>{
      if (err) {
        Toastify({
          text: err,
          duration: 3000,
          backgroundColor: 'linear-gradient(to right, #0988fe, #1c75fb)'
        }).showToast();
      }
    });

  };


  const handleUnfollow = function(e) {
    e.stopPropagation();
    unfollow(targetId)(store.dispatch, store.getState).then(([err,res])=>{
      if (err) {
        Toastify({
          text: err,
          duration: 3000,
          backgroundColor: 'linear-gradient(to right, #0988fe, #1c75fb)'
        }).showToast();
      }
    });


  };


  const icon = (<Star
    strokeWidth="15px"
    width="15px"
    height="15px"

  />);
  const iconFilled = (<StarFilled
    strokeWidth="15px"
    width="15px"
    height="15px"

  />);

  if(needText){
    if(!me){
      return(<span  className="btn bg-transparent  d-flex px-1 py-0 shadow-sm" styleName="detail-svg" data-toggle="modal" data-target="#sign" onClick={stopPropagation}>{icon}<span>订阅</span></span>)
    }else if(followList.indexOf(targetId)>-1 ){
      return(<span  className="btn bg-transparent  d-flex px-1 py-0 shadow-sm" styleName="detail-svg"  onClick={handleUnfollow}>{iconFilled}<span>取消订阅</span></span>)
    }else {
      return(<span  className="btn bg-transparent  d-flex px-1 py-0 shadow-sm" styleName="detail-svg"  onClick={handleFollow}>{icon}<span>订阅</span></span>)
    }

  }else{
    if(!me){
      return(<span  className={`btn  ${btnLight? "btn-light":null} `}  data-toggle="modal" data-target="#sign" onClick={stopPropagation}>{icon}</span>)
    }else if(followList.indexOf(targetId)>-1 ){
      return(<span  className={`btn  ${btnLight? "btn-light":null} `} onClick={handleUnfollow}>{iconFilled}</span>)
    }else {
      return(<span  className={`btn  ${btnLight? "btn-light":null} `}  onClick={handleFollow}>{icon}</span>)
    }
  }




  // if(!me){
  //   return(<button  className="btn " data-toggle="modal" data-target="#sign" onClick={stopPropagation}>{icon}{needText? `<span>订阅</span>`:null }</button>)
  // }else if(followList.indexOf(targetId)>-1 ){
  //   return(<button  className="btn "  onClick={handleUnfollow}>{iconFilled}{needText? `<span>取消订阅</span>`:null }</button>)
  // }else {
  //   return(<button  className="btn "  onClick={handleFollow}>{icon}{needText? `<span>订阅</span>`:null }</button>)
  // }




}