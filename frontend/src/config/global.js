const menuBarList = [{
  name: '接口',
  id: 'interface',
  sub: [{
    name: '工程目录',
    componentName: 'InterProjectView'
  },
  {
    name: '环境管理',
    componentName: 'LoginEnv'
  }]
},  {
  name: 'OES',
  id: 'OES',
  sub: [{
    name: 'OES项目',
    componentName: 'OESProjectView'
  }]
},{
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
  save:"save",
  getList:"getList",
  getById:"getById",
  deleteById:"deleteById",
  getProjectAndIntersByProjectId:"getProjectAndIntersByProjectId",  //根据项目获取项目及接口数据
// ------------------接口相关
  saveInterAndUpdateProject:"saveInterAndUpdateProject",  //项目内保存接口
  interInfoById:"interInfoById",  //根据id查看接口详情
  runSingleInter:"runSingleInter",  //单接口执行
// ----------------------OES相关
  saveOESProject:"saveOESProject",  //新建/保存OES项目
  getOESProjectList:"getOESProjectList",  //OES项目列表
  getOESProjectById:"getOESProjectById",  //查看OES项目详情
  deleteOESProjectById:"deleteOESProjectById",  //删除OES项目
  saveOESInter:"saveOESInter", //保存OES接口
  getOESProjectInterList:"getOESProjectInterList", //获取项目下OES接口List
  getOESInterById:"getOESInterById", //根据ID查看OES接口
  deleteOESProjectInter:"deleteOESProjectInter", //删除OES接口
  runOESInter:"runOESInter", //运行OES接口
// ----------------------VA工具相关
  insertVAProject:"insertVAProject",//新建
  getVAProjectList:"getVAProjectList",//查看VAList/查询
  updateVAProject:"updateVAProject",  //编辑VA项目
  getVAProjectsByProjectName:"getVAProjectsByProjectName",//根据项目名查看
  getVAProjectsByProjectId:"getVAProjectsByProjectId",//根据id查看VA项目详情
  deleteVAProject:"deleteVAProject",//删除VA项目
  getProjectVAList:"getProjectVAList",  //取得项目下所有VA
  insertVA:"insertVA",  //插入VA
  getProjectVA:"getProjectVA",  //查看项目下VA详情
  deleteProjectVA:"deleteProjectVA",  //删除项目下VA
  updateProjectVA:"updateProjectVA",  //更新项目下VA
}

  export default
  {
    menuBarList,
    backEndUrl,
    backEndPath
  }
