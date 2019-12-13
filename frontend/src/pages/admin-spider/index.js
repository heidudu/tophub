import React, {useEffect, useRef, useState} from 'react';
import './style.scss'
import MainColumn from '../../layout/main'
import store from "../../redux";
import Loading from "../../components/common/loading";
import {useSelector} from "react-redux";
import MaterialTable, {MTableHeader} from "material-table";
import {getAdminSpider} from '../../redux/reducers/admin';
import {loadAdminSpider, updateAdminSpider, runAdminSpider, stopAdminSpider} from '../../redux/actions/admin'
import Toastify from "toastify-js";
import {getUserInfo} from "../../redux/reducers/user";
import NotFound from '../not-found'

export default function (props) {

  const me = useSelector((state) => getUserInfo(state));
  const adminProject = useSelector((state) => getAdminSpider(state));
  const [loading,setLoading] = useState(true);


  useEffect(()=>{
    if(me) {
      loadAdminSpider()(store.dispatch, store.getState).then(function ([err, res]) {
        if (err) {
          Toastify({
            text: err,
            duration: 3000,
            backgroundColor: 'linear-gradient(to right, #0988fe, #1c75fb)'
          }).showToast()
        } else {
          setLoading(false)
        }
      });
    }else{
      setLoading(false)
    }

  },[me]);

  const tableRef = useRef(null);

  if(!me || me.role==='user'){return <NotFound />}
  else if(loading){return <MainColumn><Loading /></MainColumn> }
  else return(
    <MainColumn>
      {adminProject &&
        <MaterialTable
          title="爬虫管理"
          tableRef={tableRef}
          components={{
            Header: props => (<MTableHeader {...props} localization={{actions: " "}}/>)
          }}
          columns={[
            {title: "爬虫名称", field: "spider_name", filtering: false, editable: "never"},
            {title: "间隔时间（分钟）", field: "interval", filtering: false},
            {title: "运行状态", field: "status",  editable: "never", lookup: {1: "运行中", 0: "停止"}},
            {title: "项目名称", field: "project_name", filtering: false, editable: "never"},
            {title: "当前版本", field: "current_version", filtering: false, editable: "never"},
            {title: "历史版本", field: "history_version", filtering: false, editable: "never"},
          ]}
          data={adminProject.data}
          options={{
            selection: true,
            pageSize:20
          }}
          actions={[
            {
              tooltip: '运行',
              icon: 'play_arrow',
              onClick: (evt, data) => {
                runAdminSpider(data)(store.dispatch, store.getState).then(function ([err,res]) {

                  if(err){
                    Toastify({
                      text: "运行失败，请重试",
                      duration: 3000,
                      backgroundColor: 'linear-gradient(to right, #0988fe, #1c75fb)'
                    }).showToast();
                  }else{
                    tableRef.current.onAllSelected(false)
                  }

                });

              }
            },
            {
              tooltip: '停止',
              icon: 'pause',
              onClick: (evt, data) => {
                stopAdminSpider(data)(store.dispatch, store.getState).then(function ([err,res]) {
                  if(err){
                    Toastify({
                      text: "终止失败，请重试",
                      duration: 3000,
                      backgroundColor: 'linear-gradient(to right, #0988fe, #1c75fb)'
                    }).showToast();
                  }else{
                    tableRef.current.onAllSelected(false)
                  }
                })
              }
            },
          ]}
          editable={{
            onRowUpdate: (newData, oldData) =>{return updateAdminSpider(newData,oldData)(store.dispatch, store.getState)}

          }}


        />
      }


    </MainColumn>
  )
}