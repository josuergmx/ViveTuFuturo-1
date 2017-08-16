package com.project.vive.repository;

import java.io.Serializable;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.project.vive.entity.Rol;

@Repository("rolRepository")
public interface RolRepository extends JpaRepository<Rol, Serializable> {
	public abstract Rol findById(Integer id);
}
