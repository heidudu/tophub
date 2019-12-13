import React, {useEffect, useState} from 'react';
import './style.scss'
import MainColumn from '../../layout/main'
import './style.scss'
import AdminTable from '../../components/admin-table'
import {useSelector} from "react-redux";
import {getAdminNodes,getAdminSource, getAdminTopic} from "../../redux/reducers/admin";
import Loading from "../../components/common/loading";
import {addAdminNodes, updateAdminNodes, deleteAdminNodes,loadAdminNodes, loadAdminSource, addAdminSource, updateAdminSource, deleteAdminSource, loadAdminTopic, addAdminTopic, updateAdminTopic, deleteAdminTopic} from "../../redux/actions/admin";
import store from "../../redux";
import * as Icons from "react-feather";
import Toastify from "toastify-js";
import {getUserInfo} from "../../redux/reducers/user";
import NotFound from "../not-found";





export default function (props) {



  const adminNodes = useSelector((state) => getAdminNodes(state));
  const adminSource = useSelector((state) => getAdminSource(state));
  const adminTopic = useSelector((state) => getAdminTopic(state));
  const nodeColumns = [
    {title:"名称",field:"name",filtering:false},
    {title:"类型",field:"type",lookup:{0:"普通型",1:"热搜型"}},
    {title:"显示数量",field:"num",filtering:false},
    {title:"归属来源",field:"source_id",lookup:adminNodes? adminNodes.source_lookup:{}},
    {title:"归属主题",field:"topic_id",lookup:adminNodes? adminNodes.topic_lookup:{}},];
  const sourceColumns = [
    {title:"图标",field:"img_url",filtering:false,render:rowData =><img alt="topic_img" src={rowData.img_url} style={{width: 40,height:40, borderRadius: '50%'}}/>  },
    {title:"名称",field:"name",filtering:false},];
  const topicIconLookup = function () {
    const result={};
    for (const key in Icons){
      const  Icon = Icons[key];
      result[key]= <Icon />
    }
    return result
  };
  const topicColumns = [
    {title:"图标",field:"icon_name",filtering:false,lookup:topicIconLookup()},
    {title:"名称",field:"name",filtering:false},];
  const [nodeLoading,setNodeLoading] = useState(true);
  const [sourceLoading,setSourceLoading] = useState(true);
  const [topicLoading,setTopicLoading] = useState(true);
  const me = useSelector((state) => getUserInfo(state));

  useEffect(()=>{
    if(me && (me.role==="admin")) {
      loadAdminNodes()(store.dispatch, store.getState).then(function ([err, res]) {
        if (err) {
          Toastify({
            text: err,
            duration: 3000,
            backgroundColor: 'linear-gradient(to right, #0988fe, #1c75fb)'
          }).showToast();
        } else {
          setNodeLoading(false)
        }
      });
      loadAdminSource()(store.dispatch, store.getState).then(function ([err, res]) {
        if (err) {
          Toastify({
            text: err,
            duration: 3000,
            backgroundColor: 'linear-gradient(to right, #0988fe, #1c75fb)'
          }).showToast();
        } else {
          setSourceLoading(false)
        }
      });
      loadAdminTopic()(store.dispatch, store.getState).then(function ([err, res]) {
        if (err) {
          Toastify({
            text: err,
            duration: 3000,
            backgroundColor: 'linear-gradient(to right, #0988fe, #1c75fb)'
          }).showToast();
        } else {
          setTopicLoading(false)
        }
      });
    }
  },[me]);

  if(!me || me.role==='user'){return <NotFound />}
  else if (nodeLoading || sourceLoading || topicLoading) {return <MainColumn><Loading /></MainColumn> }
  else return(
    <MainColumn>
      <div styleName="admin-nav" role="tablist" className="nav nav-tabs d-flex justify-content-around mb-4 text-center  text-dark ">
        <a href="#admin-node" id="admin-node-tab" data-toggle="pill" styleName="nav-item" className=" active" role="tab" aria-controls="admin-node" aria-selected="true">节点管理</a>
        <a href="#admin-source" id="admin-source-tab" data-toggle="pill" styleName="nav-item" role="tab" aria-controls="admin-source" aria-selected="false">来源管理</a>
        <a href="#admin-topic" id="admin-topic-tab" data-toggle="pill" styleName="nav-item" role="tab" aria-controls="admin-topic" aria-selected="false">主题管理</a>
      </div>
      <div  className=" card flex-fill tab-pane fade  show active" id="admin-node" role="tabpanel" aria-labelledby="admin-node-tab">
        {adminNodes &&
          <AdminTable
            title="节点管理"
            columns={nodeColumns}
            data={adminNodes.data}
            AddFunction={(newData)=>{return addAdminNodes(newData)(store.dispatch, store.getState)}}
            UpdateFunction={(newData,oldData)=>{return updateAdminNodes(newData,oldData)(store.dispatch, store.getState)}}
            DeleteFunction={(oldData)=>{return deleteAdminNodes(oldData)(store.dispatch, store.getState)}}

          />}
      </div>
      <div  className=" card flex-fill tab-pane fade " id="admin-source" role="tabpanel" aria-labelledby="admin-source-tab">
        {adminSource &&
          <AdminTable
            title="来源管理"
            localization={{body:{editRow:{deleteText:"该来源没有子节点才能删除成功"}}}}
            columns={sourceColumns}
            data={adminSource.data}
            AddFunction={(newData)=>{return addAdminSource(newData)(store.dispatch, store.getState)}}
            UpdateFunction={(newData,oldData)=>{return updateAdminSource(newData,oldData)(store.dispatch, store.getState)}}
            DeleteFunction={(oldData)=>{return deleteAdminSource(oldData)(store.dispatch, store.getState)}}

          />}
      </div>
      <div  className=" card flex-fill tab-pane fade " id="admin-topic" role="tabpanel" aria-labelledby="admin-topic-tab">
        {adminTopic &&
          <AdminTable
            title="主题管理"
            localization={{body:{editRow:{deleteText:"该主题没有子节点才能删除成功"}}}}
            columns={topicColumns}
            data={adminTopic.data}
            AddFunction={(newData)=>{return addAdminTopic(newData)(store.dispatch, store.getState)}}
            UpdateFunction={(newData,oldData)=>{return updateAdminTopic(newData,oldData)(store.dispatch, store.getState)}}
            DeleteFunction={(oldData)=>{return deleteAdminTopic(oldData)(store.dispatch, store.getState)}}

          />}
      </div>

    </MainColumn>
  )
}