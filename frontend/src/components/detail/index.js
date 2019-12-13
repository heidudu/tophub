import React from 'react';
import './style.scss';
import {Link} from "react-router-dom";
import dateStr from '../../vendors/parse-time';
import FollowButton from '../common/follow'


export default function(props) {

  const {data} = props;
  return (

    <div className="p-3">
      <div className="detail-title my-3 ">
        <img styleName="detail-img"   alt="detail-img" src={data.detail.source_img}/>
        <div className="justify-content-between d-flex" >
          <span styleName="title-left">{data.detail.source_name}{data.detail.topic_name==="博客"?null:`•${data.detail.name}`}</span>
          <FollowButton targetId={data.detail.id} needText={true} />
        </div>
      </div>
      <div styleName="detail-nav" role="tablist" className="nav nav-tabs d-flex justify-content-around mb-4 text-center  text-dark ">
        <a href="#new" id="nav-new-tab" data-toggle="pill" styleName="nav-item" className=" active" role="tab" aria-controls="new" aria-selected="true">最新</a>
        <a href="#history" id="nav-history-tab" data-toggle="pill" styleName="nav-item"  role="tab" aria-controls="history" aria-selected="false">历史</a>
        <a href="#related" id="nav-related-tab" data-toggle="pill" styleName="nav-item" role="tab" aria-controls="related" aria-selected="false">相关节点</a>
      </div>
      <div  className=" card flex-fill tab-pane fade  show active" id="new" role="tabpanel" aria-labelledby="nav-new-tab">
        <div className="card-body " >
          <span className="card-title mb-3 d-flex" >最新</span>
          <div className="card-text">
            {data.detail.tops.latest?
              data.detail.tops.latest.map((item,index)=>{
              return(
                <a href={item.url} target="_blank" rel="noopener noreferrer" styleName="card-body-item" className="d-flex justify-content-between  mb-3 text-dark" key={index}>
                  <span className="text-left "  >{index+1}</span>
                  <span className=" text-left col" >{item.title}</span>
                  <span className="text-muted d-flex" style={{maxWidth:"34%",overflow:"hidden",whiteSpace:"nowrap"}}>{item.description_content}</span>
                </a>
              )
            })
            :
            null
            }
          </div>
        </div>
      </div>
      <div  className=" card flex-fill tab-pane fade" id="history" role="tabpanel" aria-labelledby="nav-history-tab">
        <div className="card-body " >
          <span className="card-title mb-3 d-flex" >历史</span>
          <div className="card-text">
            {data.detail.tops.history?
              data.detail.tops.history.map((item,index)=>{
              return(
                <a href={item.url} target="_blank" rel="noopener noreferrer" styleName="card-body-item" className="d-flex justify-content-between  mb-3 text-dark" key={index}>
                  <span className="text-left "  >{dateStr(item.time)}</span>
                  <span className=" text-left col " >{item.title}</span>
                  <span className="text-muted d-flex" style={{maxWidth:"34%",overflow:"hidden",whiteSpace:"nowrap"}}>{item.description_content}</span>
                </a>
              )
            })
            :
            null
            }
          </div>
        </div>
      </div>
      <div  className=" card flex-fill tab-pane fade" id="related" role="tabpanel" aria-labelledby="nav-related-tab">
        <div className="card-body" >
          <span className="card-title mb-3 d-flex" >相关节点</span>
          <div className="card-text">
            {data.related?
              data.related.map((item,index)=>{
              return(
                <div   className="d-flex justify-content-between  mb-3 text-dark" key={index}>
                  <Link to={`/node/${item.id}`} className="text-dark col-10 pl-0">
                    <img className="rounded-circle " styleName="related_img" alt="card-img" src={item.source_img}/><span >{item.source_name}{item.topic_name==="博客"?null:`•${item.name}`}</span>
                  </Link>
                  <FollowButton targetId={item.id}/>
                </div>
              )
            })
            :
            null
            }
          </div>
        </div>
      </div>

    </div>
  )
 }