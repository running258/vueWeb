import axios from 'axios'
import global from '@/config/global'

function getList(collectionName,searchName){
    var res = axios.get(global.backEndUrl + global.backEndPath["getList"], {
        params: {
            name: searchName,
            collectionName: collectionName
        }
    })
    return res
}

function save(jsonInfo){
    var res = axios.post(global.backEndUrl + global.backEndPath["save"],jsonInfo)
    return res
}

function getById(collectionName,_id){
    var res = axios.get(global.backEndUrl + global.backEndPath["getById"], {
        params: {
            _id: _id,
            collectionName: collectionName
        }
    })
    return res
}

function deleteById(collectionName,_id){
    var res = axios.get(global.backEndUrl + global.backEndPath["deleteById"], {
        params: {
            _id: _id,
            collectionName: collectionName
        }
    })
    return res
}

function getProjectAndIntersByProjectId(projectCollectionName,interCollectionName,_id){
    var res = axios.get(global.backEndUrl + global.backEndPath["getProjectAndIntersByProjectId"], {
        params: {
            _id: _id,
            projectCollectionName: projectCollectionName,
            interCollectionName: interCollectionName
        }
    })
    return res
}


export default{
    getList,
    save,
    getById,
    deleteById,
    getProjectAndIntersByProjectId
} 