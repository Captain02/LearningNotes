package com.micro.provider.microprovider8001.dept.controller;

import com.entity.Dept;
import com.micro.provider.microprovider8001.dept.service.DeptService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class DeptController {

    @Autowired
    DeptService deptService;

    @GetMapping("/getlist")
    public List<Dept> getList() {
        return deptService.list();
    }

}
