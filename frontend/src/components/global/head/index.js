import React, {useEffect,useState} from 'react';
import { AlignJustify, Search, Paperclip,Edit3,Edit} from 'react-feather';
import * as Icons from'react-feather'
import {Link} from "react-router-dom";
import { useSelector} from 'react-redux';
import { _signOutRequest} from "../../../api";
import { getUserInfo } from "../../../redux/reducers/user";
import  { getTopicNav } from "../../../redux/reducers/topic";
import './style.scss';
import {loadTopicNav} from "../../../redux/actions/topic";
import store from "../../../redux";
import {withRouter} from 'react-router-dom';
import {loadFollowList} from "../../../redux/actions/follow";
import Toastify from "toastify-js";
import {removeActiveSidebar,changeActiveSidebar} from "../../../redux/actions/sidebar"
import {getPcActive,getMobileActive} from "../../../redux/reducers/sidebar";


export default withRouter(function(props) {

   // const { history, location} = useReactRouter();
   const _signOut = function(e){
     e.stopPropagation();
     _signOutRequest().then(([err,res]) => {
       if (res && res.success){
         console.log('退出成功');
           window.location.reload();
         }else{
         Toastify({
           text:"退出失败",
           duration: 3000,
           backgroundColor: 'linear-gradient(to right, #0988fe, #1c75fb)'
         }).showToast();
       }
       })
   };

   const _changeActivate = function (e) {
      changeActiveSidebar()(store.dispatch, store.getState)

   };

  const _handleSubmit = function (e) {
    e.preventDefault();
    if(text === '' || text === undefined || text === null) {
      Toastify({
        text:"搜索内容不能为空",
        duration: 3000,
        backgroundColor: 'linear-gradient(to right, #0988fe, #1c75fb)'
      }).showToast();
      return "return false"
    }else{
      props.history.push("/search?q=" + text)
    }
  };


  const pcActivate = useSelector((state) => getPcActive(state));
  const mobileActivate = useSelector((state) => getMobileActive(state));
  const me = useSelector((state) => getUserInfo(state));
  const topicNav = useSelector((state) => getTopicNav(state));
  const [text, setText] = useState('');

  useEffect(()=>{
    window.addEventListener('resize', removeActiveSidebar()(store.dispatch, store.getState), false)
  });




  useEffect(()=>{
    loadTopicNav()(store.dispatch, store.getState).then(function([err,res]){
      if(err){
        Toastify({
          text: err,
          duration: 3000,
          backgroundColor: 'linear-gradient(to right, #0988fe, #1c75fb)'
        }).showToast()
      }
    })

  },[]);
  useEffect(()=>{
    loadFollowList()(store.dispatch, store.getState)

  },[me]);

  useEffect(()=>{
    if(props.location.pathname !== '/search'){
      setText('')
    }
  },[props.location.pathname]);



  return (
    <header className="fixed-top">
      <nav className="navbar  bg-white navbar-light shadow-sm d-flex px-md-4 mb-1"  styleName="top_header">
        <div className="justify-content-start d-flex  row " >
          <button className="navbar-toggler rounded-circle border-0"  id="sidebar-collapse" onClick={_changeActivate}>
            <AlignJustify />
          </button>
          <Link className="navbar-brand ml-1 ml-sm-0 font-weight-bold text-secondary" to="/">Tophub</Link>
        </div>
        <form className="justify-content-center form-inline  bg-light  rounded  col-5  " onSubmit={()=>{return false}} styleName="header-center">
          <div className="flex-fill input-group bg-transparent " >
            <button className="input-group-prepend border-0 rounded-circle bg-light " type="submit"  onClick={_handleSubmit}>
              <Search />
            </button>
            <input className="bg-transparent border-0  form-control ml-1" type="text" value={text} onChange={(e)=>{setText(e.target.value)}} />

          </div>
        </form>
        <div className=" d-flex  " >
          {
            me?
              <>
                <button href="#!" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" styleName="avatar" style={{backgroundImage:`url(${me.avatar})`}}></button>
                <div className="dropdown-menu dropdown-menu-right">
                  {/*<Link className="dropdown-item" to={`/people/${me.id}`}>我的主页</Link>*/}
                  {/*<Link className="dropdown-item" to="/settings">设置</Link>*/}
                  {/*<div className="dropdown-divider"></div>*/}
                  <a className="dropdown-item" href="#!" onClick={_signOut}>退出</a>
                </div>
              </>
              :
              <>
                <button   className="btn btn-link border-0 text-decoration-none " data-toggle="modal" data-target="#sign" data-type="sign-in" ><strong>登 录</strong></button>
              </>
          }
        </div>
      </nav>
      <nav className={`nav-stacked pt-3  bg-white ${mobileActivate?'active':null}`} styleName="mobile-sidebar"  id="mobile-sidebar">
        <div><Link to="/" className={`nav-item nav-link ${props.location.pathname ===`/`? 'active': ''}`} styleName="sidebar-item" ><Paperclip className="mx-3" />订阅</Link></div>
        {topicNav &&
          topicNav.map((item,index)=>{
            const Icon = Icons[item["icon"]];
            return(<div key={index}><Link className={`nav-item nav-link ${props.location.pathname ===`/topic/${item.id}`? 'active': ''}`} styleName="sidebar-item" to={`/topic/${item.id}`}><Icon className="mx-3"/>{item.name}</Link></div>)
          })

        }
        {
          me&&me.role === "admin"?
            <>
              <div className="divider">
                <hr/>
              </div>
              <div><Link to="/admin/node" className={`nav-item nav-link ${props.location.pathname ==='/admin/node'? 'active': ''}`} styleName="sidebar-item" ><Edit3 className="mx-3" />节点管理</Link></div>
              <div><Link to="/admin/spider" className={`nav-item nav-link ${props.location.pathname ==='/admin/spider'? 'active': ''}`} styleName="sidebar-item" ><Edit className="mx-3" />爬虫管理</Link></div>
            </>
            :
            null
        }
      </nav>
      <nav className={`nav-stacked pt-3  bg-white ${pcActivate?'active':null}`} styleName="pc-sidebar"  id="pc-sidebar">
        <div><Link  to="/" className={`nav-item nav-link ${props.location.pathname ===`/`? 'active': ''}`} styleName="sidebar-item" ><Paperclip className="mx-3" />订阅</Link></div>
        {topicNav &&
          topicNav.map((item,index)=>{
            const Icon = Icons[item["icon"]];
            return(<div key={index}><Link className={`nav-item nav-link ${props.location.pathname ===`/topic/${item.id}`? 'active': ''}`} styleName="sidebar-item" to={`/topic/${item.id}`}><Icon className="mx-3"/>{item.name}</Link></div>)
          })
        }
        {
          me&&me.role === "admin"?
            <>
              <div className="divider"><hr /></div>
              <div><Link to="/admin/node" className={`nav-item nav-link ${props.location.pathname ==='/admin/node'? 'active': ''}`} styleName="sidebar-item" ><Edit3 className="mx-3" />节点管理</Link></div>
              <div><Link to="/admin/spider" className={`nav-item nav-link ${props.location.pathname ==='/admin/spider'? 'active': ''}`} styleName="sidebar-item" ><Edit className="mx-3" />爬虫管理</Link></div>
            </>
            :
            null

        }
      </nav>

    </header>
  )
})