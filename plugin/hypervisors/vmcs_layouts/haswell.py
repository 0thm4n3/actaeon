
 #
 # VMCS Memory layout converted from Google Rekall Repository with
 # rekall2actaeon.py 
 #
 # Authors: 
 # Mariano `emdel` Graziano - graziano@eurecom.fr
 #
 # This program is free software; you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation; either version 2 of the License, or (at
 # your option) any later version.
 #
 # This program is distributed in the hope that it will be useful, but
 # WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 # General Public License for more details.
 #
 # You should have received a copy of the GNU General Public License
 # along with this program; if not, write to the Free Software
 # Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
 #



vmcs = {
"PAGEFAULT_ERRCODE_MATCH": 0x4d,
"HOST_IA32_PAT_HIGH": 0xc5,
"VIRTUAL_APIC_PAGE_ADDR_HIGH": 0xb1,
"APIC_ACCESS_ADDR": 0xbc,
"IO_RIP": 0x6e,
"GUEST_FS_BASE": 0x22,
"GUEST_IA32_EFER_HIGH": 0x45,
"GUEST_IDTR_BASE": 0x2e,
"CR0_READ_SHADOW": 0x94,
"ENTRY_EXCEPTION_ERROR_CODE": 0x55,
"HOST_SS_SEL": 0x31,
"GUEST_VMX_PREEMTION_TIMER": 0x58,
"HOST_IA32_SYSENTER_CS": 0xde,
"GUEST_SS_ATTR": 0x10,
"GUEST_ACTIVITY_STATE": 0x4f,
"IDT_VECTORING_INFO_FIELD": 0x5e,
"GUEST_FS_ATTR": 0x20,
"HOST_DS_SEL": 0x31,
"EXIT_MSR_LOAD_COUNT": 0x5a,
"ENTRY_MSR_LOAD_ADDR_HIGH": 0xbb,
"GUEST_IA32_SYSENTER_EIP": 0x7e,
"PAGEFAULT_ERRCODE_MASK": 0x4c,
"IO_BITMAP_A": 0xb2,
"IDT_VECTORING_ERRCODE": 0x5f,
"VMREAD_BITMAP_ADDRESS": 0xe4,
"ABORT_INDICATOR": 0x1,
"GUEST_IDTR_LIMIT": 0x2d,
"CR4_READ_SHADOW": 0x96,
"GUEST_IA32_SYSENTER_CS": 0x80,
"GUEST_IA32_PAT_HIGH": 0x43,
"IS_SHADOW_VMCS": 0x0,
"EPT_POINTER": 0x50,
"GUEST_PENDING_DEBUG_EXCEPT": 0x7a,
"GUEST_ES_BASE": 0xa,
"HOST_FS_BASE": 0xd4,
"HOST_FS_SEL": 0x32,
"GUEST_PDPTE2": 0x8c,
"GUEST_PHYSICAL_ADDR": 0x52,
"EPTP_LIST_ADDRESS": 0xe2,
"HOST_CR3": 0xcc,
"HOST_CR0": 0xca,
"HOST_CR4": 0xce,
"GUEST_TR_ATTR": 0x1c,
"GUEST_PDPTE2_HIGH": 0x8d,
"REVISION_ID": 0x0,
"GUEST_CS_BASE": 0xe,
"GUEST_RFLAGS": 0x78,
"EOI_EXIT_BITMAP_0": 0xa4,
"HOST_IA32_EFER_HIGH": 0xc7,
"IO_RCX": 0x68,
"IO_BITMAP_B_HIGH": 0xb5,
"GUEST_SS_BASE": 0x12,
"GUEST_IA32_SYSENTER_ESP": 0x7c,
"ENTRY_MSR_LOAD_ADDR": 0xba,
"EXIT_INSTR_LEN": 0x60,
"GUEST_IA32_DEBUGCTL": 0x40,
"GUEST_LDTR_ATTR": 0x18,
"HOST_ES_SEL": 0x30,
"EXIT_INTERRUPT_INFO": 0x5c,
"VMWRITE_BITMAP_ADDRESS_HIGH": 0xe7,
"GUEST_LDTR_LIMIT": 0x19,
"GUEST_DS_LIMIT": 0x15,
"GUEST_RIP": 0x76,
"GUEST_IA32_PERF_CTL": 0x46,
"EPTP_LIST_ADDRESS_HIGH": 0xe3,
"GUEST_TR_LIMIT": 0x1d,
"VPID": 0x33,
"INSTR_INFO": 0x61,
"GUEST_GDTR_LIMIT": 0x29,
"GUEST_DS_BASE": 0x16,
"GUEST_DS_ATTR": 0x14,
"CR3_TARGET_3": 0x9e,
"HOST_TR_SEL": 0x33,
"CR3_TARGET_1": 0x9a,
"CR3_TARGET_0": 0x98,
"HOST_GS_BASE": 0xd6,
"GUEST_FS_LIMIT": 0x21,
"EOI_EXIT_BITMAP_3": 0xbc,
"IO_RDI": 0x6c,
"MSR_BITMAP_HIGH": 0xbf,
"EOI_EXIT_BITMAP_1_HIGH": 0xb0,
"EXIT_CONTROLS": 0x57,
"IO_RSI": 0x6a,
"ENTRY_INSTR_LENGTH": 0x56,
"GUEST_ES_LIMIT": 0x9,
"GUEST_GS_BASE": 0x26,
"GUEST_CS_ATTR": 0xc,
"HOST_CS_SEL": 0x30,
"VMREAD_BITMAP_ADDRESS_HIGH": 0xe5,
"ENTRY_INT_INFO_FIELD": 0x54,
"GUEST_INTERRUPT_STATUS": 0x1c,
"GUEST_LDTR_BASE": 0x1a,
"GUEST_PDPTE3_HIGH": 0x8f,
"GUEST_CS_SEL": 0xc,
"TPR_THRESHOLD": 0x4b,
"TSC_OFFSET_HIGH": 0x65,
"GUEST_DS_SEL": 0x14,
"GUEST_LINEAR_ADDR": 0x70,
"HOST_IA32_SYSENTER_EIP": 0xdc,
"GUEST_ES_ATTR": 0x8,
"VM_FUNCTION_CTRL": 0xe0,
"EXIT_REASON": 0x5b,
"GUEST_PHYSICAL_ADDR_HIGH": 0x53,
"HOST_IA32_EFER": 0xc6,
"GUEST_GS_LIMIT": 0x25,
"EOI_EXIT_BITMAP_1": 0xac,
"GUEST_GS_SEL": 0x24,
"APIC_ACCESS_ADDR_HIGH": 0xbd,
"GUEST_SMBASE": 0xaa,
"HOST_IA32_PAT": 0xc4,
"EOI_EXIT_BITMAP_2": 0xb4,
"PLE_WINDOW": 0x3d,
"HOST_GS_SEL": 0x32,
"CR3_TARGET_COUNT": 0xad,
"HOST_RSP": 0xc0,
"HOST_RIP": 0xc2,
"PROC_VM_EXEC_CONTROLS2": 0x49,
"EXIT_MSR_STORE_ADDR": 0xb6,
"IO_BITMAP_A_HIGH": 0xb3,
"EXECUTIVE_VMCS_PTR": 0x34,
"HOST_IA32_PERF_CTL": 0xc8,
"VM_FUNCTION_CTRL_HIGH": 0xe1,
"HOST_TR_BASE": 0xd8,
"GUEST_CS_LIMIT": 0xd,
"EXIT_QUALIFICATION": 0x66,
"EXIT_INTERRUPT_ERRCODE": 0x5d,
"GUEST_FS_SEL": 0x20,
"PLE_GAP": 0x3c,
"PROC_VM_EXEC_CONTROLS": 0x48,
"GUEST_PDPTE1_HIGH": 0x8b,
"GUEST_LDTR_SEL": 0x18,
"HOST_GDTR_BASE": 0xd2,
"VE_INFO_ADDRESS": 0xdc,
"ENTRY_CONTROLS": 0xae,
"GUEST_PDPTE0_HIGH": 0x89,
"GUEST_IA32_PAT": 0x42,
"CR3_TARGET_2": 0x9c,
"GUEST_GS_ATTR": 0x24,
"GUEST_TR_SEL": 0x1c,
"HOST_IA32_SYSENTER_ESP": 0xda,
"GUEST_IA32_DEBUGCTL_HIGH": 0x41,
"IO_BITMAP_B": 0xb4,
"EOI_EXIT_BITMAP_0_HIGH": 0xa8,
"GUEST_PDPTE0": 0x88,
"EPT_POINTER_HIGH": 0x51,
"GUEST_GDTR_BASE": 0x2a,
"INSTR_ERROR": 0x3,
"VIRTUAL_APIC_PAGE_ADDR": 0xb0,
"GUEST_PDPTE3": 0x8e,
"GUEST_CR0": 0x82,
"GUEST_CR3": 0x84,
"GUEST_CR4": 0x86,
"HOST_IDTR_BASE": 0xd0,
"GUEST_PDPTE1": 0x8a,
"EXIT_MSR_LOAD_ADDR": 0xb8,
"CR4_MASK": 0x92,
"ENTRY_MSR_LOAD_COUNT": 0xaf,
"GUEST_IA32_EFER": 0x44,
"PIN_VM_EXEC_CONTROLS": 0x4a,
"VMWRITE_BITMAP_ADDRESS": 0xe6,
"GUEST_SS_SEL": 0x10,
"HOST_IA32_PERF_CTL_HIGH": 0xc9,
"GUEST_DR7": 0x72,
"GUEST_SS_LIMIT": 0x11,
"CR0_MASK": 0x90,
"EXECUTIVE_VMCS_PTR_HIGH": 0x35,
"VMCS_LINK_PTR": 0x3e,
"GUEST_ES_SEL": 0x8,
"VMCS_LINK_PTR_HIGH": 0x3f,
"MSR_BITMAP": 0xbe,
"GUEST_IA32_PERF_CTL_HIGH": 0x47,
"EOI_EXIT_BITMAP_2_HIGH": 0xb8,
"EXIT_MSR_STORE_ADDR_HIGH": 0xb7,
"EXIT_MSR_LOAD_ADDR_HIGH": 0xb9,
"GUEST_RSP": 0x74,
"TSC_OFFSET": 0x64,
"EXCEPTION_BITMAP": 0xac,
"EOI_EXIT_BITMAP_3_HIGH": 0xc0,
"GUEST_INTERRUPTIBILITY_INFO": 0x4e,
"VE_INFO_ADDRESS_HIGH": 0xe0,
"EXIT_MSR_STORE_COUNT": 0x59,
"GUEST_TR_BASE": 0x1e
}
