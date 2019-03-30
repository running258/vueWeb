const menuBarList = [{
  name: '接口',
  id: 'interface',
  sub: [{
    name: '工程目录',
    componentName: 'Project'
  },
  {
    name: '环境管理',
    componentName: 'LoginEnv'
  }]
}, {
  name: 'VirtualAsset',
  id: 'VA',
  sub: [{
    name: 'VA项目列表',
    componentName: 'VAProject'
  }]
}]



const backEndUrl = "http://localhost:5000/"
// const backEndUrl = "http://192.168.96.28:90/"
const backEndPath = {
  getProject:"getProjects",   //获取所有项目
  insertNewProject:"insertNewProject",  //新建项目
  getProjectAndIntersByProjectName:"getProjectAndIntersByProjectName",  //项目中添加新接口
  interInfoById:"interInfoById",  //根据id查看接口详情
  runSingleInter:"runSingleInter",  //单接口执行
  saveInterAndUpdateProject:"saveInterAndUpdateProject",  //项目内保存接口
  updateLoginEnv:"updateLoginEnv",  //环境保存
  getAllLoginEnv:"getAllLoginEnv",  //获取所有环境
// ----------------------VA工具相关
  insertVAProject:"insertVAProject",//新建
  getVAProjectList:"getVAProjectList",//查看VAList/查询
  getVAProjectsByProjectName:"getVAProjectsByProjectName",//根据项目名查看
  getProjectVAList:"getProjectVAList",  //取得项目下所有VA
  insertVA:"insertVA",  //插入VA

  updateVA:"updateVA",  //更新VA
  getVA:"getVA",  //查看VA
  deleteVA:"deleteVA",  //删除VA
}

  export default
  {
    menuBarList,
    backEndUrl,
    backEndPath
  }