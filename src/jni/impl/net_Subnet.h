// ==================================================================
// @(#)net_Subnet.h
//
// @author Bruno Quoitin (bruno.quoitin@uclouvain.be)
// @date 19/10/2007
// $Id: net_Subnet.h,v 1.3 2008-04-11 11:03:06 bqu Exp $
//
// C-BGP, BGP Routing Solver
// Copyright (C) 2002-2008 Bruno Quoitin
//
// This program is free software; you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation; either version 2 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program; if not, write to the Free Software
// Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
// 02111-1307  USA
// ==================================================================

#ifndef __JNI_NET_SUBNET_H__
#define __JNI_NET_SUBNET_H__

#include <jni_md.h>
#include <jni.h>

#ifdef __cplusplus
extern "C" {
#endif

  // -----[ cbgp_jni_new_net_Subnet ]----------------------------------
  jobject cbgp_jni_new_net_Subnet(JNIEnv * jEnv, jobject joCBGP,
				  net_subnet_t * subnet);

#ifdef __cplusplus
}
#endif

#endif /* __JNI_NET_SUBNET_H__ */