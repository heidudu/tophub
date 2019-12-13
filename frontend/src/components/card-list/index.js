import React,{useEffect} from 'react';
import './style.scss';
 import {ArrowRight} from 'react-feather'
import {Link} from "react-router-dom";
// import "./card"
import FollowButton from '../common/follow'
import $ from "jquery";


 function SingleCard(props) {
  const {index,item} = props;
  useEffect(()=>{
    window.addEventListener('resize', function () {
      if(window.innerWidth>767){
        $('.collapse').collapse('show');
      }else{
        $('.collapse').collapse('hide');
      }
    }, false)
  });

  return (
    <div className="card-box p-1  col-xs-12 col-sm-6 col-md-4 col-lg-3 " styleName="card-box" id={index} >
      <div className="card text-center shadow-sm  px-0 ">
        <div className="btn-group bg-light " role="group" styleName="card-header" >
          <FollowButton targetId={item.id} btnLight={true} />
          <span  className="btn btn-light  col-11 d-flex px-0" data-toggle="collapse" data-target={"#test-" + index } style={{overflow:"hidden",whiteSpace:"nowrap"}}>
            <div className="text-center " ><img styleName="card-img"  alt="card-img" src={item.source_img}/><strong >{item.source_name}{item.topic_name==="博客"?null:`•${item.name}`}</strong></div>
          </span>
          <Link to={`/node/${item.id}`}  className="btn btn-light" >
            <ArrowRight/>
          </Link>
        </div>
        {/*<div className="pb-2 accordion-body collapse  " id={"test-" + index}>*/}
        <div className={window.innerWidth>767?"pb-2 accordion-body collapse show":"pb-2 accordion-body collapse" } id={"test-" + index}>
          <div className="card-body p-1 " >
            {item.tops.latest.map((top,index)=>{
              return(
                <a href={top.url} target="_blank" rel="noopener noreferrer" styleName="card-body-item" className="d-flex justify-content-between  mb-1 " key={index}>
                  {index<3? <span className="text-danger text-center "  style={{width:"7%"}}>{index+1}</span>:<span className="text-dark text-center" style={{width:"7%"}}>{index+1}</span>}
                  <span className="col  text-dark text-left px-1" styleName="card-body-item-content">{top.title}</span>
                  <span className="text-muted" styleName="card-body-item-content" style={{maxWidth:"34%",overflow:"hidden",whiteSpace:"nowrap"}}>{top.description_content}</span>
                </a>
              )
            })}
          </div>
        </div>

      </div>
    </div>
  )
}

export default function(props) {
  const {list=[]} = props;

  return (
    <div className="row mx-0 justify-content-center p-1 "  >
      {list.map((item,index) => (
        <SingleCard index={String(index)} key={String(index)} item={item} />
      ))}
      {/*用于最后一行对齐*/}
      <i className="  col-xs-12 col-sm-6 col-md-4 col-lg-3 " key="empty-1"></i>
      <i className="  col-xs-12 col-sm-6 col-md-4 col-lg-3 " key="empty-2"></i>
      <i className="  col-xs-12 col-sm-6 col-md-4 col-lg-3 " key="empty-3"></i>
    </div>
  )
}