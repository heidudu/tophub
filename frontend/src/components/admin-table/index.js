import React,{useCallback} from 'react';
import MaterialTable, {MTableHeader} from "material-table";








 function AdminTable(props) {
   const {title,columns,data,AddFunction,UpdateFunction,DeleteFunction,options={filtering:true},localization={body:{editRow:{deleteText:"确定要删除吗？"}}}}=props;
   return(
      <MaterialTable
        components={{
          Header:props=>(<MTableHeader {...props} localization={{actions:"操作"}} />)
        }}
        title={title}
        columns={columns}
        localization={localization}
        data={data}
        options={options}
        editable={{
          onRowAdd:useCallback((newData) =>{return AddFunction(newData)},[AddFunction] ),
          onRowUpdate:useCallback((newData, oldData) =>{return UpdateFunction(newData, oldData)},[UpdateFunction] ),
          onRowDelete:useCallback((oldData) =>{return DeleteFunction(oldData)},[DeleteFunction] ),


        }}
      />
   )
 }

 export default AdminTable