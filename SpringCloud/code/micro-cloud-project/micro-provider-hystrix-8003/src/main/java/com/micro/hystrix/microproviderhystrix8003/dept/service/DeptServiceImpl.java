package com.micro.hystrix.microproviderhystrix8003.dept.service;

import com.entity.Dept;
import com.micro.hystrix.microproviderhystrix8003.dept.dao.DeptDao;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class DeptServiceImpl implements DeptService {

    @Autowired
    DeptDao deptDao;

    @Override
    public List<Dept> list() {
        return deptDao.selectlist();
    }
}
