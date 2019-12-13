import React, {useEffect,useState} from 'react';
import './style.scss'
import CenterColumn from '../../layout/center-column'
import Detail from '../../components/detail'
import './style.scss'
import store from "../../redux";
import { useSelector} from 'react-redux';
import {getNodeDetail} from "../../redux/reducers/node";
import {setNodeDetail} from "../../redux/actions/node"
import Loading from "../../components/common/loading"
import Toastify from "toastify-js";





export default function (props) {

  const id = props.match.params.id;
  const nodeDetail = useSelector((state) => getNodeDetail(state));
  const [loading,setLoading] = useState(true);

  useEffect(()=>{
    setLoading(true);
    setNodeDetail(id)(store.dispatch, store.getState).then(function([err,res]){
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
  },[id]);

  if(loading){return <CenterColumn><Loading /></CenterColumn> }
  else return(
    <CenterColumn>
      {nodeDetail && <Detail data={nodeDetail} />}
    </CenterColumn>
  )
}